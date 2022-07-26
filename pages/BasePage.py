from resorses.pars_values import getDataFromConfig
from tests_utils.session import Session


class BasePage(object):

    def __init__(self, base_url=getDataFromConfig('BASE_URL')):
        self.base_url = base_url
        self.browser = Session.get_driver()
        self.timeout = 30

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def visit(self, url):
        self.browser.get(url)

    def go_out(self):
        self.browser.quit()
