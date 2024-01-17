from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup


class Strategy(ABCMeta):
    @abstractmethod
    def execute(self, source_page: str):
        pass
