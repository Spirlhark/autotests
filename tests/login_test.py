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
class TestLoginExaminationHeaderHome:
    def test_examination_header_home(self):
        sign_in = SignInPage()
        sign_in.examination()


@pytest.mark.usefixtures("start_session")
class TestSecurity:
    def test_security(self):
        test_security = SecurityPage()
        test_security.tabSecurity()
        test_security.openRecentSecurity()
        test_security.openActivity()


@pytest.mark.usefixtures("start_session")
class TestSecurityExaminationFormProfile:
    def test_examination_form_profile(self):
        test_security = SecurityPage()
        test_security.examination()


@pytest.mark.usefixtures("start_session")
class TestPerson:
    def test_person(self):
        test_person = PersonalInfoPage()
        test_person.tabPersonal()


@pytest.mark.usefixtures("start_session")
class TestPersonExaminationPersonalInfo:
    def test_examination_personal_info(self):
        test_person = PersonalInfoPage()
        test_person.examination()


@pytest.mark.usefixtures("start_session")
class TestPeople:
    def test_people(self):
        test_people = PeopleSharingPage()
        test_people.tabPeopleSharing()
        test_people.openContacts()


@pytest.mark.usefixtures("start_session")
class TestPeopleExaminationOpenContactsPage:
    def test_examination_open_contact_page(self):
        test_people = PeopleSharingPage()
        test_people.examination()
