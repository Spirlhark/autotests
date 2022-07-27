from pages.BasePage import BasePage
import allure
from selenium.webdriver.common.by import By
from resorses.pars_values import getDataFromConfig


class SecurityPage(BasePage):
    locator_dictionary = {
        "tabSecurityPage": (By.CSS_SELECTOR, ".HJOYVi11"),
        "openRecentSecurityActivityList": (By.PARTIAL_LINK_TEXT, 'Посмотреть действия'),
        "openActivityDetails": (By.PARTIAL_LINK_TEXT, 'Новое'),
        "formProfile": (By.XPATH, '//*[@id="yDmH0d"]/c-wiz[3]/div/div[2]/div[2]/c-wiz/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]')
        }

    @allure.step("Tab Security Page")
    def tabSecurity(self):
        self.find_element(*self.locator_dictionary['tabSecurityPage']).click()

    @allure.step("Open Recent Security Activity List")
    def openRecentSecurity(self):
        self.find_element(*self.locator_dictionary['openRecentSecurityActivityList']).click()

    @allure.step("Open Activity Details")
    def openActivity(self):
        self.find_element(*self.locator_dictionary['openActivityDetails']).click()

    @allure.step('Check form Profile')
    def examination(self):
        text = getDataFromConfig('REGION') + ' ' + getDataFromConfig('COUNTRY')
        assert self.find_element(*self.locator_dictionary['formProfile']).text == text
