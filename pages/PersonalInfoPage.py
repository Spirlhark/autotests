import time
from pages.BasePage import BasePage
import allure
from selenium.webdriver.common.by import By


class PersonalInfoPage(BasePage):
    locator_dictionary = {
        "tabPersonalInfo": (By.XPATH, "/html/body/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[1]/div[3]/c-wiz/nav/ul/li[2]/a")
        # "menuGender": (By.XPATH, '')
        }

    @allure.step("Tab Personal Info")
    def tabPersonal(self):
        self.visit(self.base_url)
        time.sleep(2)
        self.find_element(*self.locator_dictionary['tabPersonalInfo']).click()
        # self.find_element(*self.locator_dictionary['menuGender']).click()
