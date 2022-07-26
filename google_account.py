from selenium import webdriver
import undetected_chromedriver as vc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

from resorses.pars_values import getDataFromConfig
import time

print(getDataFromConfig('TEXT'))
print(getDataFromConfig('FIRST_NAME'))
print(getDataFromConfig('LAST_NAME'))


text = getDataFromConfig('TEXT') + " " + getDataFromConfig('FIRST_NAME') + ' ' + getDataFromConfig('LAST_NAME')+'!'

print(text)

driver = vc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)

driver.get('https://www.google.com/account/about/?hl=ru')
driver.maximize_window()
in_account = driver.find_element(By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a')
in_account.click()
time.sleep(1)
email = driver.find_element(By.ID, 'identifierId').send_keys('xsxtestxsx97@gmail.com')
time.sleep(3)
nextBtn = driver.find_element(By.ID, 'identifierNext').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('7rHXgT7LU4qGwms')
nextbtn2 = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
time.sleep(5)
in_account = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/header/h1').text
# print(type(in_account))
# print(in_account)
driver.find_element(By.CSS_SELECTOR, ".HJOYVi11").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Посмотреть действия').click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Новое').click()
time.sleep(30)
# security = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[4]/div/div[2]/div[2]/c-wiz/div/div/div/div[2]/div[2]/div/h1')
security = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[3]/div/div[2]/div[2]/c-wiz/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]')
# security = driver.find_element(By.CSS_SELECTOR, '#yDmH0d > c-wiz:nth-child(22) > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div > div > div > div.s2HbZc.lUJWSb > div.hjhf2e > div > div.COyG6c > div:nth-child(2) > div.FVYsnd > div.C1b4sb')
secur = security.text
print(type(secur))
print(secur)
