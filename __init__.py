from Parser import Parser
from WebDriver import WebDriver

if __name__ == '__main__':
    url = ''
    webdriver = WebDriver()
    parser = Parser()
    webdriver.open_url(url)
    # parser.parse(webdriver.get_page_source())
    print(webdriver.get_page_source())
