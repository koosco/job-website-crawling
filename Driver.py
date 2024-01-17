from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class BrowserManager:
    def __init__(self, headless=True, no_sandbox=True):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        if no_sandbox:
            chrome_options.add_argument('--no-sandbox')
        chrome_options.add_experimental_option('detach', True)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(options=chrome_options)
        handles = self.driver.window_handles
        for handle in handles:
            if handle != handles[0]:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(handles[0])

    def open_url(self, url: str) -> str:
        self.driver.get(url)
        page_source = self.driver.page_source

        return page_source

    def close_url(self):
        self.driver.close()
