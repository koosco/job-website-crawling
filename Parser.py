from strategy.incruit.IncruitStrategy import IncruitStrategy
from strategy.jobkorea.JobkoreaStrategy import JobkoreaStrategy
from strategy.saramin.SaraminStrategy import SaraminStrategy
from strategy.wanted.WantedStrategy import WantedStrategy
from strategy.worknet.WorknetStrategy import WorknetStrategy
from post import Post


class Parser:
    def __init__(self):
        self.strategies = [IncruitStrategy(), JobkoreaStrategy(), SaraminStrategy(),
                           WantedStrategy(), WorknetStrategy()]
        self.strategy_idx = 0
        self.strategy = self.strategies[self.strategy_idx]

    def get_next_strategy(self) -> None:
        self.strategy_idx += 1
        if self.strategy_idx >= len(self.strategies):
            self.strategy_idx = 0
        self.strategy = self.strategies[self.strategy_idx]

    def parse(self, source_page: str) -> Post:
        return self.strategy.execute(source_page)

