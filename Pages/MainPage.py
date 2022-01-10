import time

from APP_testdemo.Pages.BasePage import BasePage
import APP_testdemo.CustomLogger as cl


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators in Main Page
    _allowdevicelocation_button = "com.android.packageinstaller:id/permission_allow_button"
    _denydevicelocation_button = "com.android.packageinstaller:id/permission_deny_button"
    _selectcountry_button = "Netherlands"
    _locationbutton = "com.takeaway.android:id/locationButton"
    _deliverybutton = "//android.widget.LinearLayout[@content-desc='Delivery']"
    _pickupbutton = "//android.widget.TextView[@content-desc='Pickup'"
    _accmenubutton = "//android.widget.ImageButton[@content-desc='Account menu. Shows side bar with advanced options']"
    _viewpersonalinfo = "View personal information"
    _signinbutton = "Sign in"
    _createaccountbutton = "Create account"
    _inboxbutton = "Inbox"
    _ordersbutton = "Orders"
    _favsbutton = "Favourites"
    _paybutton = "Pay"
    _puntenbutton = "Punten"
    _giftcardsbutton = "Gift cards"
    _needhelpbutton = "Need help?"
    _faqbutton = "Frequently asked questions"
    _termsandcondbutton = "Terms and conditions"
    _privpolbutton = "Privacy policy"
    _colophonbutton = "Colophon"
    _custsuppbutton = "Customer support"
    _countrybutton = "Country"
    _languagebutton = "Language"
    _becomeacourierbutton = "Become a courier"
    _searchforlocation_textbox = "com.takeaway.android:id/searchInput"
    _backfromsearchlocation_button = "//android.widget.ImageButton[@content-desc='Back. Returns to the previous page']"

    def allowance_devicelocation(self):
        self.clickElement(self.allowance_devicelocation, "id")
        cl.allurelogs("Device location allowed!")
        time.sleep(1)

    def click_selectcountry(self):
        self.clickElement(self._selectcountry_button, "text")
        cl.allurelogs("Clicked on the country 'Netherlands'")

    def click_pickupbutton(self):
        self.clickElement(self._pickupbutton, "id")
        cl.allurelogs("Clicked on 'Pickup' button")

    def click_deliverybutton(self):
        self.clickElement(self._deliverybutton, "id")
        cl.allurelogs("Clicked on 'Delivery' button")

    def click_locationbutton(self):
        self.clickElement(self._locationbutton, "text")
        cl.allurelogs("Clicked on 'Select your location' button")

    def click_accmenubutton(self):
        self.clickElement(self._accmenubutton, "xpath")
        cl.allurelogs("Clicked on 'Account Menu' button")

    def click_viewpersonalinfo(self):
        self.clickElement(self._viewpersonalinfo, "text")
        cl.allurelogs("Clicked on 'View personal information' button")

    def click_signinbutton(self):
        self.clickElement(self._signinbutton, "text")
        cl.allurelogs("Clicked on 'Signin' button")

