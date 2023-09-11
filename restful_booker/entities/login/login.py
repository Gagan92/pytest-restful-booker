from restful_booker.core.base import Base


class Login(Base):

    def __init__(self, request):
        super().__init__(request)
        self.data = {}
        self.login_resp = None

    def login_to_booker_api(self, login):

        password = self.constants['USERS'][login.upper()]['PASSWORD']
        username = self.constants['USERS'][login.upper()]['LOGINID']

        ##USE THE BELOW CODE IN ORDER TO CREATE THE TOKEN
        # message = username + ':' + password
        # message_bytes = message.encode('ascii')
        # base64_bytes = base64.b64encode(message_bytes)
        # token = 'Basic ' + base64_bytes.decode('ascii')

        self = super().login_user_with_credentials(username, password)
        from restful_booker.core.restful_booker import Restful_Booker
        return Restful_Booker(self.request)