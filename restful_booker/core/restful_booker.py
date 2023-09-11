from restful_booker.entities.book.book import Books
from restful_booker.entities.ping.ping import Ping
from restful_booker.entities.login.login import Login


class Restful_Booker:

    def __init__(self, request):
        self.request = request

    def Login(self):
        return Login(self.request)

    def Books(self):
        return Books(self.request)

    def Ping(self):
        return Ping(self.request)