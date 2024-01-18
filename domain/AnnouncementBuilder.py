from Announcement import Announcement


class AnnouncementBuilder:
    idx = 0

    def __init__(self):
        self.announcement = Announcement()

    def company(self, company):
        self.announcement.company = company
        return self

    def company_size(self, company_size):
        self.announcement.company_size = company_size
        return self

    def post_name(self, post_name):
        self.announcement.post_name = post_name
        return self

    def career(self, career):
        self.announcement.career = career
        return self

    def education(self, education):
        self.announcement.education = education
        return self

    def location(self, location):
        self.announcement.location = location
        return self

    def work_type(self, work_type):
        self.announcement.work_type = work_type
        return self

    def url(self, url):
        self.announcement.url = url
        return self

    def build(self):
        self.announcement.idx = AnnouncementBuilder.idx
        AnnouncementBuilder.idx += 1
        return self
