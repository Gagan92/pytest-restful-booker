from abc import ABCMeta, abstractmethod
from importlib import import_module
# from bs4 import BeautifulSoup
from jinja2.nativetypes import NativeEnvironment
from core.http_wrapper import HttpWrapper


class Base(metaclass=ABCMeta):
    def _generate_payload(func):
        def template_wrapper(self, entity, data=None, json=None, status_code=200, **kwargs):
            details = json or data
            payload = details.get('payload', 'default')

            if isinstance(payload, str):
                payload_filename = details.get('payload_file')
                payload_file_path = f'restful_booker.entities.{entity}.payloads.{payload_filename}'

                template_module = import_module(payload_file_path)
                payload_section_name = details.get('payload', 'default')
                payload_from_section = getattr(template_module, payload_section_name)
                payload_from_section = self.env.from_string(str(payload_from_section))
                payload = payload_from_section.render(details)

            if json:
                json['payload'] = payload
                data = {'payload': None}
            else:
                data['payload'] = payload
                json = {'payload': None}
            return func(self, entity, data, json, status_code, **kwargs)

        return template_wrapper

    def __init__(self, request):
        self.request = request
        self.constants = request.getfixturevalue('read_connectors')
        self.cmd_options = request.getfixturevalue('set_cmdline_opts')
        # self.db_store = request.getfixturevalue('tiny_db_store')
        # self.test_id = request.config.option.test_id
        self.scope = request.scope
        self.http_wrapper = HttpWrapper(request)
        self.env = NativeEnvironment()
        self.urls = request.getfixturevalue('read_urls')

    def _generate_url(self, entity, data):
        """
        Mandatory keys in data
        url_action : Function will get the url from urls.yml
        or
        url: Function will expect to have a url in data
        """
        return data.get('url')

    @_generate_payload
    def post(self, entity, data=None, json=None, status_code=200, **kwargs):
        url = self._generate_url(entity, data)

        return self.http_wrapper.post(
            url, data.get('payload'), json.get('payload'), status_code, **kwargs
        )

    @_generate_payload
    def put(self, entity, data=None, json=None, status_code=201, **kwargs):
        url = self._generate_url(entity, data)

        return self.http_wrapper.put(
            url, data.get('payload'), json.get('payload'), status_code, **kwargs
        )

    def get(self, entity, data, status_code=200, **kwargs):
        url = self._generate_url(entity, data)
        return self.http_wrapper.get(url, status_code=status_code, **kwargs)
    def login_user_with_credentials(self, user_id, password):

        api = self.urls['Auth']['create_token']
        url = api.format(protocol=self.constants['SERVER']['PROTOCOL'],
                         env=self.cmd_options['env'])
        self.data.update({ 'payload_file': 'login', 'payload': 'default'})

        ## ADD HEADERS IF NEEDED
        # headers = {"Authorization": token}
        # self.http_wrapper.post(url=url, headers=headers, status_code=204)

        self.http_wrapper.post(url=url, data=self.data,status_code=200)
        cookie_dict = self.http_wrapper.session.cookies.get_dict()
        self.request.config.aspxauth = cookie_dict[".ASPXAUTH"]
        return self

