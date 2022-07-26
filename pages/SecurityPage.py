import time
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
        time.sleep(2)

    @allure.step("Open Recent Security Activity List")
    def openRecentSecurity(self):
        self.find_element(*self.locator_dictionary['openRecentSecurityActivityList']).click()
        time.sleep(2)

    @allure.step("Open Activity Details")
    def openActivity(self):
        self.find_element(*self.locator_dictionary['openActivityDetails']).click()

    @allure.step('Check form Profile')
    def examination(self):
        qwerty = self.find_element(*self.locator_dictionary['formProfile']).text
        if check() == 'Добро пожаловать, Тест Тест!':
    #         return print('\n' + "!!!!!!!!!!!!!" + '\n' + "Текст совпадает =)" + '\n' + '!!!!!!!!!!!!!')
    #     else:
    #         return print("АшеПка")




        # text = 'Днепропетровская область, Украина'
        # if qwerty == text:
        #     return True
        # else:
        #     return False