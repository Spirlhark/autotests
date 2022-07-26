import time
from pages.BasePage import BasePage
import allure
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    locator_dictionary = {
        "buttonGoToGoogleAccount": (By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a'),
        "fieldEmail": (By.XPATH, '//*[@id="identifierId"]'),
        "fieldPassword": (By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'),
        "buttonNextOnPasswordForm": (By.XPATH, '//*[@id="identifierNext"]/div/button/span'),
        "buttonNextOnHomePage": (By.XPATH, '//*[@id="passwordNext"]/div/button/span'),
        # "headerHome": (By.CSS_SELECTOR, 'header h1')
        # "headerHome": (By.PARTIAL_LINK_TEXT, 'Добро пожаловать, Тест Тест!')
        "headerHome": (By.XPATH, '//*[@id="gb"]/div[2]/div[3]/div[1]/div[2]/div/a')
        }

    @allure.step("Go to Sign In")
    def login(self):
        self.visit(self.base_url)
        self.find_element(*self.locator_dictionary['buttonGoToGoogleAccount']).click()

    @allure.step("Send Username")
    def sendEmail(self, username):
        self.find_element(*self.locator_dictionary['fieldEmail']).send_keys(username)
        self.find_element(*self.locator_dictionary['buttonNextOnPasswordForm']).click()
        time.sleep(2)

    @allure.step("Send Password")
    def sendPassword(self, passwd):
        self.find_element(*self.locator_dictionary['fieldPassword']).send_keys(passwd)
        self.find_element(*self.locator_dictionary['buttonNextOnHomePage']).click()
        time.sleep(2)

    @allure.step('')
    def сheckHeaderHomePage(self):
        self.find_element(*self.locator_dictionary['headerHome']).text





    # @allure.step("go out browser")
    # def out(self):
    #     self.go_out()







