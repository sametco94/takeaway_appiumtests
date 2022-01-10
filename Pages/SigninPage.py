from APP_testdemo.Pages.BasePage import BasePage
import APP_testdemo.CustomLogger as cl


class SigninPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators in Signin Page
    _signinviagoogle = "com.takeaway.android:id/googleButton"
    _signinviafacebook = "com.takeaway.android:id/facebookButton"
    _emailorusername_texbox = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText"
    _password_texbox = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText"
    _forgotpasswordbutton = "Forgot password?"
    _signinbutton = "com.takeaway.android:id/loginConfirmButton"
    _createaccountbutton = "com.takeaway.android:id/loginSignupButton"
    _closesigninbutton = "//android.widget.ImageButton[@content-desc='Navigate up']"

    def click_signinviagoogle(self):
        self.clickElement(self._signinviagoogle, "id")
        cl.allurelogs("Clicked on 'Sign in with Google Button")

    def click_signinviafacebooke(self):
        self.clickElement(self._signinviafacebook, "id")
        cl.allurelogs("Clicked on 'Sign in with Facebook' Button")

    def enter_usernameandpass(self):
        self.sendText("testmail@testmail.com", self._emailorusername_texbox, "xpath")
        self.sendText("12345678910", self._password_texbox, "index")
        cl.allurelogs("Email or username and then password entered!")

    def click_forgotpass(self):
        self.clickElement(self._forgotpasswordbutton, "text")
        cl.allurelogs("Clicked on 'Forgot password?' Button")

    def click_signinbutton(self):
        self.clickElement(self._signinbutton, "id")
        cl.allurelogs("Clicked on 'Signin' Button")

    def click_createaccountbutton(self):
        self.clickElement(self._createaccountbutton, "id")

    def click_closepage(self):
        self.clickElement(self._closesigninbutton, "xpath")
