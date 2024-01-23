from bs4 import BeautifulSoup
from Strategy import Strategy
from PostBuilder import PostBuilder


class IncruitStrategy(Strategy):
    def __init__(self):
        self.pages = 1

    def execute(self, source_page: str):
        builder = PostBuilder()
        tags = []
        soup = BeautifulSoup(source_page, 'html.parser')
        content_list = soup.find('div', {'class': 'cBbslist_contenst'})
        contents = content_list.find_all('ul', {'class': 'c_row'})

        for content in contents:
            cell_first = content.find('div', {'class': 'cell_first'})
            cell_mid = content.find('div', {'class': 'cell_mid'})
            cell_last = content.find('div', {'class': 'cell_last'})

            company_name = cell_first.find('a', {'class': 'cpname'}).text  # 회사명
            post_name = cell_mid.find('div', {'class': 'cl_top'}).find('a').text  # 공고명

            spec = cell_mid.find('div', {'class': 'cl_md'}).find_all('span')
            career = spec[0].text  # 경력
            education = spec[1].text  # 교육수준
            location = spec[2].text  # 지역
            work_type = spec[3].text  # 직무형태

            company_tags = cell_mid.find('div', {'class': 'cl_btm'}).find_all('span')

            for tag in company_tags:
                tags.append(tag.text)

            deadline = cell_last.find('span')
            res = (builder.
                   company(company_name).
                   post_name(post_name).
                   career(career).
                   education(education).
                   location(location).
                   work_type(work_type).
                   deadline(deadline).build())
            print('회사명:', res.company)
            print('공고명:', res.post_name)
            print('경력:', res.career)
            print('교육수준:', res.education)
            print()
        return None
