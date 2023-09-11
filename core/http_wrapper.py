import requests


# TODO: Verify the Status code in each of the http methods
class HttpWrapper:

    def __init__(self, request):
        self.request = request
        self.session = requests.session()

   
    def get(self, url, status_code, **kwargs):
        return self.session.get(url, **kwargs)

   
    def post(self, url, data=None, json=None, status_code=None, *args, **kwargs):
        return self.session.post(url, data=data, json=json, **kwargs)

   
    def put(self, url, data, json, status_code, **kwargs):
        return self.session.put(url, data=data, json=json, **kwargs)

   
    def delete(self, url, data, json=None, status_code=None, **kwargs):
        return self.session.delete(url, data=data, json=json, **kwargs)

   
    def patch(self, url, data, json=None, status_code=None, **kwargs):
        return self.session.patch(url, data=data, json=json, **kwargs)
