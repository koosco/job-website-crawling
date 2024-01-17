from Parser import Parser
from WebDriver import WebDriver

if __name__ == '__main__':
    url = 'https://job.incruit.com/jobdb_list/searchjob.asp?ct=3&ty=1&cd=149'
    webdriver = WebDriver()
    parser = Parser()
    webdriver.open_url(url)
    parser.parse(webdriver.get_page_source())
