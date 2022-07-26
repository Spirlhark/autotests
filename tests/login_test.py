import time

import pytest
from pages.SignInPage import SignInPage
from pages.SecurityPage import SecurityPage
from pages.PersonalInfoPage import PersonalInfoPage
from pages.PeopleSharingPage import PeopleSharingPage
from resorses.pars_values import getDataFromConfig


@pytest.mark.usefixtures("start_session")
class TestLogin:
    def test_sign_in(self):
        sign_in = SignInPage()
        sign_in.login()
        sign_in.sendEmail(getDataFromConfig('EMAIL'))
        sign_in.sendPassword(getDataFromConfig('PASSWORD'))


@pytest.mark.usefixtures("start_session")
class TestExaminationS:
    def test_examination(self):
        sign_in = SignInPage()
        sign_in.examination()
        time.sleep(2)


@pytest.mark.usefixtures("start_session")
class TestSecurity:
    def test_security(self):
        test_security = SecurityPage()
        test_security.tabSecurity()
        test_security.openRecentSecurity()
        test_security.openActivity()


@pytest.mark.usefixtures("start_session")
class TestExaminationS:
    def test_examination(self):
        test_security = SecurityPage()
        test_security.examination()



# @pytest.mark.usefixtures("start_session")
# class TestPerson:
#     def test_person(self):
#         test_person = PersonalInfoPage()
#         test_person.tabPersonal()
#
#
# @pytest.mark.usefixtures("start_session")
# class TestPeople:
#     def test_people(self):
#         test_people = PeopleSharingPage()
#         test_people.tabPeopleSharing()
#         test_people.openContacts()
