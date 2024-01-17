from abc import abstractmethod
from typing import List

from strategy.Strategy import Strategy

from strategy.incruit.IncruitStrategy import IncruitStrategy
from strategy.jobkorea.JobkoreaStrategy import JobkoreaStrategy
from strategy.saramin.SaraminStrategy import SaraminStrategy
from strategy.wanted.WantedStrategy import WantedStrategy
from strategy.worknet.WorknetStrategy import WorknetStrategy
import json


class Parser:
    def __init__(self):
        self.__init_strategy()
        self.strategy_idx = 0
        self.strategy = self.strategies[self.strategy_idx]

    def __init_strategy(self):
        base_urls = json.loads('./resources/urls')
        self.strategies: List[Strategy] = \
            [IncruitStrategy(base_urls['incruit']), JobkoreaStrategy(base_urls['jobkorea']),
             SaraminStrategy(base_urls['saramin']), WantedStrategy(base_urls['wanted']),
             WorknetStrategy(base_urls['worknet'])]

    def get_next_strategy(self):
        self.strategy_idx += 1
        self.strategy = self.strategies[self.strategy_idx]

    @abstractmethod
    def parse(self, source_page: str):
        self.strategy.execute(source_page)
