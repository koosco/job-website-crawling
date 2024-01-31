from bs4 import BeautifulSoup
from Strategy import Strategy
from domain.post.PostBuilder import PostBuilder


class IncruitStrategy(Strategy):
    def __init__(self):
        self.posts = []

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


if __name__ == '__main__':
    from repository.post.MemoryPostRepository import MemoryPostRepository
    from ParamPrinter import ParamPrinter
    with open('/Users/koo/Desktop/git/job-webset-crawling/src/resources/incruit/job_collect.html') as file:
        source = file.read()
    strategy = IncruitStrategy()
    items = strategy.execute(source)
    # for item in items:
    #     ParamPrinter.print_class_params(item)
    MemoryPostRepository.save_posts(items)
