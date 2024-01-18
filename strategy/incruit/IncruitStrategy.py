from bs4 import BeautifulSoup

from ..Strategy import Strategy


class IncruitStrategy(Strategy):
    def execute(self, source_page: str):
        soup = BeautifulSoup(source_page, 'html.parser')
        res = soup.find_all('ul', {'class': 'c_row'})
        for i, r in enumerate(res):
            print(i, r.text)
