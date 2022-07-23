import pytest
import undetected_chromedriver as vc
from pages.SignInPage import SignIn
from tests_utils.session import Session
from resorses.pars_values import getDataFromConfig

driver = vc.Chrome(use_subprocess=True)

# print(base_url())
# print(value_email())
# print(value_password())


@pytest.mark.usefixtures("start_session")
class TestLogin:
    def test_log_in(self):
        SignIn(Session.get_driver(), getDataFromConfig('BASE_URL')).login(getDataFromConfig('EMAIL'), getDataFromConfig('PASSWORD'))


