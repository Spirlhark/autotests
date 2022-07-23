import time

import allure
from selenium.webdriver.common.by import By


class SignIn(object):
    locator_dictionary = {
        "go": (By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a'),
        "email": (By.XPATH, '//*[@id="identifierId"]'),
        # "password": (By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'),
        # "password": (By.XPATH, "//attribute::*[contains(., 'current-password')]/.."),
        # "password": (By.XPATH, "//attribute::*[contains(., 'YPqjbf')]/.."),
        # "password": (By.XPATH, "//attribute::*[contains(., 'Введите пароль')]/.."),
        # "password": (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/div'),
        # "password": (By.NAME, "password"),
        # "password": (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"),
        # "password": (By.XPATH, '//*[contains(@input,"password")]'),
        "signin_button_E": (By.XPATH, '//*[@id="identifierNext"]/div/button/span'),
        "signin_button_P": (By.XPATH, '//*[@id="passwordNext"]/div/button/span')
        }

    def __init__(self, browser, base_url):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 30

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def visit(self, base_url):
        self.browser.get(base_url)

    @allure.step("Login")
    def login(self, username, passwd):
        self.visit(self.base_url)
        self.find_element(*self.locator_dictionary['go']).click()
        self.find_element(*self.locator_dictionary['email']).send_keys(username)
        self.find_element(*self.locator_dictionary['signin_button_E']).click()
        time.sleep(2)
        self.find_element(*self.locator_dictionary['password']).send_keys(passwd)
        self.find_element(*self.locator_dictionary['signin_button_P']).click()

#
# class LoginPage:
#     def __init__(self):
#         self.go = fined_element(By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a')
#         self.username = (By.XPATH, '//*[@id="identifierId"]')
#         self.password = (By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
#         self.sing_in_btn_e = (By.XPATH, '//*[@id="identifierNext"]/div/button/span')
#         self.sing_in_btn_p = (By.XPATH, '//*[@id="passwordNext"]/div/button/span')
#
#     def go(self):
#         self.go.click()
#
#     def enter_username(self, username):
#         self.username.enter_text(username)
#
#     def click_sing_in_e(self):
#         self.sing_in_btn_e.click()
#
#     def enter_password(self, password):
#         self.password.enter_text(password)
#
#     def click_sing_in_p(self):
#         self.sing_in_btn_p.click()





