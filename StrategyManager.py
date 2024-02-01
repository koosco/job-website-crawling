from strategy.incruit.IncruitStrategy import IncruitStrategy
from WebDriver import WebDriver
from post import Post


class StrategyManager:
    """
    페이지 유형에 따라 페이지를 파싱함
    """

    def __init__(self, display: bool = False):
        self.strategies = [IncruitStrategy()]
        self.strategy_idx = 1
        self.strategy = self.strategies[self.strategy_idx]
        webdriver = WebDriver(display, display)

    def get_next_strategy(self) -> None:
        self.strategy_idx += 1
        if self.strategy_idx >= len(self.strategies):
            self.strategy_idx = 0
        self.strategy = self.strategies[self.strategy_idx]

    # def parse(self) -> Post:
    #     return self.strategy.execute()
