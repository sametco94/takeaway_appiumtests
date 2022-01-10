import unittest
import pytest
import APP_testdemo.CustomLogger as cl
from APP_testdemo.Pages.BasePage import BasePage
from APP_testdemo.Pages.MainPage import MainPage
from APP_testdemo.Pages.SigninPage import SigninPage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class SigninPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.bp = BasePage(self.driver)
        self.mp = MainPage(self.driver)
        self.sip = SigninPage(self.driver)

    @pytest.mark.run(order=1)
    def test_signinpageactions(self):
        cl.allurelogs("App Launched")
        self.mp.click_accmenubutton()
        self.mp.click_signinbutton()
        self.sip.enter_usernameandpass()


