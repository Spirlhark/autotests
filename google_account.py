from selenium import webdriver
import undetected_chromedriver as vc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

from resorses.pars_values import getDataFromConfig
import time

# print(getDataFromConfig('TEXT'))
# print(getDataFromConfig('FIRST_NAME'))
# print(getDataFromConfig('SITY') + ' ' + getDataFromConfig('COUNTRY'))


# text = getDataFromConfig('TEXT') + " " + getDataFromConfig('FIRST_NAME') + ' ' + getDataFromConfig('LAST_NAME')+'!'
# text = getDataFromConfig('SITY') + ' ' + getDataFromConfig('COUNTRY')

# print(text)

driver = vc.Chrome(use_subprocess=True)
driver.implicitly_wait(20)
# wait = WebDriverWait(driver, 20)

driver.get('https://www.google.com/account/about/?hl=ru')
driver.maximize_window()
in_account = driver.find_element(By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a')
in_account.click()
# time.sleep(1)
email = driver.find_element(By.ID, 'identifierId').send_keys('xsxtestxsx97@gmail.com')
# time.sleep(3)
nextBtn = driver.find_element(By.ID, 'identifierNext').click()
# time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('7rHXgT7LU4qGwms')
nextbtn2 = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
in_account = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/header/h1').text
print(type(in_account))
print(in_account)
# time.sleep(5)
if in_account == 'Добро пожаловать, Тест Тест! 123':
    print('\n' + "!!!!!!!!!!!!!" + '\n' + "Текст совпадает =)" + '\n' + '!!!!!!!!!!!!!')
else:
    print("АшеПка")



# driver.find_element(By.CSS_SELECTOR, ".HJOYVi12").click()
# time.sleep(3)
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Начать').click()
# time.sleep(3)
# in_account = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div[1]/div[1]/div[1]/h1').text
# in_account = driver.find_element(By.CSS_SELECTOR, '#yDmH0d > c-wiz:nth-child(20) > div > div:nth-child(2) > div.EWuRAb.OUzXuf > div.ikIPKb > div.edoSyc.MGyuR > h1').text
# print(type(in_account))
# print(in_account)
# print(driver.current_url)
# '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div[1]/div[1]/div[1]/h1'

# driver.find_element(By.CSS_SELECTOR, ".HJOYVi11").click()
# time.sleep(2)
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Посмотреть действия').click()
# time.sleep(2)
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Новое').click()
# time.sleep(30)
# security = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[3]/div/div[2]/div[2]/c-wiz/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]')
# secur = security.text
# print(type(secur))
# print(secur)


# @allure.step('Check Header Home Page')
# def examination(self):
#     if check() == 'Добро пожаловать, Тест Тест!':
#         return print('\n' + "!!!!!!!!!!!!!" + '\n' + "Текст совпадает =)" + '\n' + '!!!!!!!!!!!!!')
#     else:
#         return print("АшеПка")
