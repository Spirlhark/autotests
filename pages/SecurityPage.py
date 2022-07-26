import time
from pages.BasePage import BasePage
import allure
from selenium.webdriver.common.by import By


class SecurityPage(BasePage):
    locator_dictionary = {
        "tabSecurityPage": (By.CSS_SELECTOR, ".HJOYVi11"),
        "openRecentSecurityActivityList": (By.PARTIAL_LINK_TEXT, 'Посмотреть действия'),
        "openActivityDetails": (By.PARTIAL_LINK_TEXT, 'Новое')
        # "formProfile": (By.XPATH, '//*[@id="identifierNext"]/div/button/span')
        }

    @allure.step("Tab Security Page")
    def tabSecurity(self):
        self.find_element(*self.locator_dictionary['tabSecurityPage']).click()
        time.sleep(2)

    @allure.step("Open Recent Security Activity List")
    def openRecentSecurity(self):
        self.find_element(*self.locator_dictionary['openRecentSecurityActivityList']).click()
        time.sleep(2)

    @allure.step("Open Activity Details")
    def openActivity(self):
        self.find_element(*self.locator_dictionary['openActivityDetails']).click()
