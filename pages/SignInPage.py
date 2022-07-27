from pages.BasePage import BasePage
import allure
from selenium.webdriver.common.by import By
from resorses.pars_values import getDataFromConfig
import unittest


class SignInPage(BasePage):
    locator_dictionary = {
        "buttonGoToGoogleAccount": (By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a'),
        "fieldEmail": (By.XPATH, '//*[@id="identifierId"]'),
        "fieldPassword": (By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'),
        "buttonNextOnPasswordForm": (By.XPATH, '//*[@id="identifierNext"]/div/button/span'),
        "buttonNextOnHomePage": (By.XPATH, '//*[@id="passwordNext"]/div/button/span'),
        "headerHome": (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/header/h1')
        }

    @allure.step("Go to Sign In")
    def login(self):
        self.visit(self.base_url)
        self.find_element(*self.locator_dictionary['buttonGoToGoogleAccount']).click()

    @allure.step("Send Username")
    def sendEmail(self, username):
        self.find_element(*self.locator_dictionary['fieldEmail']).send_keys(username)
        self.find_element(*self.locator_dictionary['buttonNextOnPasswordForm']).click()

    @allure.step("Send Password")
    def sendPassword(self, passwd):
        self.find_element(*self.locator_dictionary['fieldPassword']).send_keys(passwd)
        self.find_element(*self.locator_dictionary['buttonNextOnHomePage']).click()

    @allure.step('Check Header Home Page')
    def examination(self):
        text = getDataFromConfig('GREETING') + " " + getDataFromConfig('FIRST_NAME') + ' ' + getDataFromConfig(
            'LAST_NAME') + '!'
        assert self.find_element(*self.locator_dictionary['headerHome']).text == text
