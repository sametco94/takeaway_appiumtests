import allure
from allure_commons.types import AttachmentType
import APP_testdemo.CustomLogger as cl
import time


class CreateaccountPageClass:

    log = cl.customlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.signinviagoogle = driver.find_element_by_android_uiautomator('id("com.takeaway.android:id/googleButton")')
        self.signinviafacebook = driver.find_element_by_android_uiautomator('id("com.takeaway.android:id/facebookButton")')
        self.name_texbox = driver.find_element_by_android_uiautomator('xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText")')
        self.emailorusername_textbox = driver.find_element_by_android_uiautomator('xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText")')
        self.password_texbox = driver.find_element_by_android_uiautomator('xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.EditText")')
        self.confirmpassword_textbox = driver.find_element_by_android_uiautomator('xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.EditText")')
        self.subscribe_checkbox = driver.find_element_by_android_uiautomator('id("com.takeaway.android:id/signupSubscribeCheckbox")')
        self.createaccountbutton = driver.find_element_by_android_uiautomator('id("com.takeaway.android:id/signupConfirmButton")')
        self.alreadygotaccountbutton = driver.find_element_by_android_uiautomator('id("com.takeaway.android:id/signupLoginButton")')
        self.closecreateaccountbutton = driver.find_element_by_android_uiautomator('xpath("//android.widget.ImageButton[@content-desc="Navigate up"]")')

    def click_signinviagoogle(self):
        self.signinviagoogle.click()
        cl.allurelogs("Click on 'Sign in with Google' Button")

    def click_signinviafacebook(self):
        self.signinviafacebook.click()
        cl.allurelogs("Click on 'Sign in with Facebook' Button")

    def enter_name(self, name):
        self.name_texbox.sendText(name)

    def enter_emailorusername(self, emailorusername):
        self.emailorusername_textbox.sendText(emailorusername)

    def enter_password(self, password):
        self.password_texbox.sendText(password)

    def confirm_password(self, confirmpass):
        self.confirmpassword_textbox.sendText(confirmpass)

    def click_subscribecheckbox(self):
        self.subscribe_checkbox.click()
        cl.allurelogs("Click on 'Yes, I want to receive discounts, loyalty offers, and other updates.' Checkbox")

    def click_createaccount(self):
        self.createaccountbutton.click()
        cl.allurelogs("Click on 'Crate account' Button")

    def click_alreadygotaccount(self):
        self.alreadygotaccountbutton.click()
        cl.allurelogs("Click on 'I already have an account' Button")

    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)

        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)

    def takeScreenshot(self,text):
        allure.attach(self.driver.get_screenshot_as_png(),name=text, attachment_type=AttachmentType.PNG)
