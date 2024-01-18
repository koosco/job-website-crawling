from Post import Post


class PostBuilder:
    def __init__(self):
        self.post = Post()

    def company(self, company):
        self.post.company = company
        return self

    def company_size(self, company_size):
        self.post.company_size = company_size
        return self

    def post_name(self, post_name):
        self.post.post_name = post_name
        return self

    def career(self, career):
        self.post.career = career
        return self

    def education(self, education):
        self.post.education = education
        return self

    def location(self, location):
        self.post.location = location
        return self

    def work_type(self, work_type):
        self.post.work_type = work_type
        return self

    def deadline(self, deadline):
        self.post.deadline = deadline
        return self

    def url(self, url):
        self.post.url = url
        return self

    def build(self):
        return self.post
