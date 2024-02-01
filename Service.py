from scheduler.Scheduler import Scheduler
from WebDriver import WebDriver


class Service:
    def __init__(self):
        self.scheduler = Scheduler()
        self.webdriver = WebDriver()

    def