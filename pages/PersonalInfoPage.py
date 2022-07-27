from pages.BasePage import BasePage
import allure
from selenium.webdriver.common.by import By
from resorses.pars_values import getDataFromConfig


class PersonalInfoPage(BasePage):
    locator_dictionary = {
        "tabPersonalInfo": (By.XPATH, "/html/body/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[1]/div[3]/c-wiz/nav/ul/li[2]/a"),
        "name": (By.XPATH, '//*[@id="c13"]/div/div[2]/div/div')
        }

    @allure.step("Tab Personal Info")
    def tabPersonal(self):
        self.visit(self.base_url)
        self.find_element(*self.locator_dictionary['tabPersonalInfo']).click()

    @allure.step('Check form Personal Info')
    def examination(self):
        text = getDataFromConfig('FIRST_NAME') + ' ' + getDataFromConfig('LAST_NAME')
        assert self.find_element(*self.locator_dictionary['name']).text == text
