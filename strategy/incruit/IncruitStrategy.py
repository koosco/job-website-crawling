from bs4 import BeautifulSoup
from Strategy import Strategy
from WebDriver import WebDriver
from domain.post.PostBuilder import PostBuilder
from collections import defaultdict
import json


class IncruitStrategy(Strategy):
    def __init__(self):
        self.posts = []
        self.base_url = None
        self.url = None
        self.params = defaultdict(str)
        self.webdriver = WebDriver()
        self.source_page = None

        with open("incruit_config.json") as config_file:
            configs = json.load(config_file)
            self.base_url = configs['base_url']
            for key, value in configs.items():
                if not key.startswith('url') and not key.endswith('url'):
                    self.params[key] = value
            self.set_param()
        self.set_source_page()
        print(self.url)

    def set_param(self):
        param_list = []
        for key, value in self.params.items():
            param_list.append(key + '=' + self.params[key])
        self.url = self.base_url + '&'.join(param_list)

    def execute(self, **kwargs):
        builder = PostBuilder()
        tags = []
        soup = BeautifulSoup(self.source_page, 'html.parser')
        content_list = soup.find('div', {'class': 'cBbslist_contenst'})
        contents = content_list.find_all('ul', {'class': 'c_row'})

        for content in contents:
            cell_first = content.find('div', {'class': 'cell_first'})
            cell_mid = content.find('div', {'class': 'cell_mid'})
            cell_last = content.find('div', {'class': 'cell_last'})

            company_name = cell_first.find('a', {'class': 'cpname'}).text  # 1. 회사이름
            post = cell_mid.find('div', {'class': 'cl_top'}).find('a')  # 2. 공고명
            post_name = post.text
            url = post.get('href')  # 2. 공고명

            spec = cell_mid.find('div', {'class': 'cl_md'}).find_all('span')
            career = spec[0].text  # 3. 경력
            education = spec[1].text  # 4. 교육
            location = spec[2].text  # 5. 지역
            job_type = spec[3].text  # 6. 채용 형태

            company_tags = cell_mid.find('div', {'class': 'cl_btm'}).find_all('span')

            for tag in company_tags:
                tags.append(tag.text)

            dates = cell_last.find_all('span')  # 7. 마감
            deadline = dates[0].text
            created_at = dates[1].text

            post_item = (builder.
                         company_name(company_name).
                         post_name(post_name).
                         career(career).
                         education(education).
                         location(location).
                         job_type(job_type).
                         deadline(deadline).
                         created_at(created_at).
                         url(url).build())
            self.posts.append(post_item)
        return self.posts

    def find_next_page(self):
        self.params['page'] = str(int(self.params['page']) + 1)
        self.set_param()
        self.set_source_page()

    def set_source_page(self):
        self.webdriver.open_url(self.url)
        self.source_page = self.webdriver.get_page_source()
