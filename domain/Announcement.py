class Announcement:
    def __init__(self):
        self.__idx = None
        self.__company = None
        self.__company_size = None
        self.__post_name = None
        self.__career = None
        self.__education = None
        self.__location = None
        self.__work_type = None
        self.__url = None

    @property
    def idx(self):
        return self.__idx

    @idx.setter
    def idx(self, idx):
        self.__idx = idx

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company):
        self.__company = company

    @property
    def company_size(self):
        return self.__company_size

    @company_size.setter
    def company_size(self, company_size):
        self.__company_size = company_size

    @property
    def post_name(self):
        return self.__post_name

    @post_name.setter
    def post_name(self, post_name):
        self.__post_name = post_name

    @property
    def career(self):
        return self.__career

    @career.setter
    def career(self, career):
        self.__career = career

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, education):
        self.__education = education

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def work_type(self):
        return self.__work_type

    @work_type.setter
    def work_type(self, work_type):
        self.__work_type = work_type

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url
