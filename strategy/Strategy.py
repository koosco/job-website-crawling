from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, source_page: str):
        pass
