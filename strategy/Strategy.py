from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, source_page: str):
        pass

    @abstractmethod
    def find_next_page(self):
        pass

    @abstractmethod
    def set_source_page(self):
        pass
