from strategy.incruit.IncruitStrategy import IncruitStrategy
from strategy.jobkorea.JobkoreaStrategy import JobkoreaStrategy
from strategy.saramin.SaraminStrategy import SaraminStrategy
from strategy.wanted.WantedStrategy import WantedStrategy
from strategy.worknet.WorknetStrategy import WorknetStrategy


class Parser:
    def __init__(self):
        self.strategy = IncruitStrategy()
        # self.strategies = None
        # self.__init_strategies()
        # self.strategy_idx = 0
        # self.strategy = self.strategies[self.strategy_idx]

    # def __init_strategies(self):
        # incruit_strategy = IncruitStrategy()
        # jobkorea_strategy = JobkoreaStrategy()
        # saramin_strategy = SaraminStrategy()
        # wanted_strategy = WantedStrategy()
        # worknet_strategy = WorknetStrategy()
        # self.strategies = \
        #     [incruit_strategy, jobkorea_strategy, saramin_strategy,
        #         wanted_strategy, worknet_strategy]

    # def get_next_strategy(self) -> None:
    #     self.strategy_idx += 1
    #     if self.strategy_idx >= len(self.strategies):
    #         self.strategy_idx = 0
    #     self.strategy = self.strategies[self.strategy_idx]

    def parse(self, source_page: str) -> None:
        # self.strategy.execute(source_page)
        print(self.strategy)
