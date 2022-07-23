from pages.SignInPage import LoginPage
from tests_utils.session import Session


import yaml
with open('prod_conf.yaml', 'r') as f: doc = yaml.load(f)


# class LoginSteps:
#     def __init__(self):
#         self.login = LoginPage()
#
#     def go_click(self):
#         self.login.go()
#
#     def send_text_username(self, username):
#         self.login.enter_username(username)
#
#     def click_sing_in_e(self):
#         self.login.click_sing_in_e()
#
#     def send_text_password(self, password):
#         self.login.enter_password(password)
#
#     def click_sing_in_p(self):
#         self.login.sing_in_btn_p()

    # def all(self):
    #     LoginPage.go()
    #     LoginPage.enter_username()
    #     LoginPage.click_sing_in_e()
    #     LoginPage.enter_password()
    #     LoginPage.click_sing_in_p()
