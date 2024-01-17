from bs4 import BeautifulSoup

from .. import Strategy


class IncruitStrategy(Strategy):
    def __init__(self, url: str):
        self.base_url = url
    def execute(self, source_page: str):
        soup = BeautifulSoup(source_page, 'html.parser')
        res = soup.find_all('div', {'class': 'cl_top'})
        for i, r in enumerate(res):
            print(i, r.text)
