from restful_booker.core.base import Base


class Books(Base):

    def __init__(self, request):
        super().__init__(request)
        self.data = {}
