from selenium import webdriver
import undetected_chromedriver as vc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time

from selenium_stealth import stealth

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")

## options.add_argument("--headless")

# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(options=options)


driver = vc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
# driver = webdriver.Chrome()
url = 'https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

# stealth(driver,
#         user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
#         languages=["ru", "ru"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         run_on_insecure_origins = False,
#         )


driver.get(url)
driver.maximize_window()
# in_account = driver.find_element(By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a')
# in_account.click()
# time.sleep(1)

email = driver.find_element(By.ID, 'identifierId').send_keys('xsxtestxsx97@gmail.com')
time.sleep(3)
nextBtn = driver.find_element(By.ID, 'identifierNext').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('7rHXgT7LU4qGwms')
nextbtn2 = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
time.sleep(20)


# class SingIn:
#     email = 'xsxtestxsx97@gmail.com'
#     password = ''
#
#     def signin(email, password):
#         driver.find_element(By.ID, 'identifierId').send_keys(email)
#         nextBtn = driver.find_element(By.ID, 'identifierNext').click()
#         driver.find_element(By.ID, 'identifierId').send_keys(password)
#         nextBtn = driver.find_element(By.ID, 'identifierNext').click()
#
# SingIn.signin(email)


# buttonGoToGoogleAcount = driver.find_element(By.CSS_SELECTOR, '.h-c-header__cta > ul > li.h-c-header__cta-li.h-c-header__cta-li--primary')
# buttonGoToGoogleAcount = driver.find_element(By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a')
# fieldEmail = driver.find_element(By.ID, '#identifierId')
# buttonNextOnEmailForm = driver.find_element(By.ID, '#identifierNext')
# fieldPassword = driver.find_element(By.NAME, 'password')
# buttonNextOnPasswordForm = driver.find_element(By.ID, '#passwordNext')

________________________________


# buttonGoToGoogleAcount1 = vc.Chrome(use_subprocess=True)
# but2 = buttonGoToGoogleAcount1.find_element(By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a')

# class SingIn:
    # email = 'xsxtestxsx97@gmail.com'
    # password = '7rHXgT7LU4qGwms'

    # _buttonGoToGoogleAcount1 = WebElement(By.ID, '.h-c-header__cta > ul > li.h-c-header__cta-li.h-c-header__cta-li--primary')
    # _buttonGoToGoogleAcount = WebElement(By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a').click()
    # buttonGoToGoogleAcount2 = buttonGoToGoogleAcount1.find_element(By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a')
    # _fieldEmail1 = WebElement(By.ID, '#identifierId')
    # _buttonNextOnEmailForm1 = WebElement(By.ID, '#identifierNext')
    # _fieldPassword1 = WebElement(By.NAME, 'password')
    # _buttonNextOnPasswordForm1 = WebElement(By.ID, '#passwordNext')

def singin(email, password):
    driver.get('https://www.google.com/account/about/?hl=ru')
    driver.find_element(By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a').click()
    # driver.find_element(By.ID, '#identifierId').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(email)
    time.sleep(2)
    # driver.find_element(By.ID, '#identifierNext').click()
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    time.sleep(2)
    # driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys(password)
    # driver.find_element(By.ID, '#passwordNext').click()
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(20)
        # self._fieldEmail1.send_keys(self.email)
        # self.buttonNextOnEmailForm1.click()
        # time.sleep(2)
        # self.fieldPassword1.send_keys(self.password)
        # self.buttonNextOnPasswordForm1.click()
        # time.sleep(10)


class SignIn:
    # locator_dictionary = {
    #     "go": (By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a'),
    #     "email": (By.XPATH, '//*[@id="identifierId"]'),
    #     "password": (By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'),
    #     "signin_button_E": (By.XPATH, '//*[@id="identifierNext"]/div/button/span'),
    #     "signin_button_P": (By.XPATH, '//*[@id="passwordNext"]/div/button/span')
    #     }

    go = (By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a')
    email = (By.XPATH, '//*[@id="identifierId"]')
    password = (By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
    signin_button_E = (By.XPATH, '//*[@id="identifierNext"]/div/button/span')
    signin_button_P = (By.XPATH, '//*[@id="passwordNext"]/div/button/span')


    def login(self):
        driver.find_element(SignIn.go).click()
        driver.find_element(SignIn.email).send_keys('xsxtestxsx97@gmail.com')
        driver.find_element(SignIn.signin_button_E).click()
        driver.find_element(SignIn.password).send_keys('7rHXgT7LU4qGwms')
        driver.find_element(SignIn.signin_button_P).click()
