import time
import unittest
import pytest
from APP_testdemo.Driver.Driver import Driver
from APP_testdemo.Pages.BasePage import BasePage
from APP_testdemo.Pages.MainPage import MainPage
import APP_testdemo.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class MainPageTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classObjects(self):
        driver = Driver()
        self.driver = driver.getDriverMethod()
        self.bp = BasePage(self.driver)
        self.mp = MainPage(self.driver)

    @pytest.mark.run(order=1)
    def test_selectcountry(self):
        cl.allurelogs("App Launched")
        time.sleep(2)
        self.mp.click_selectcountry()
        time.sleep(2)
        cl.allurelogs("'Netherlands' selected.")

    @pytest.mark.run(order=2)
    def test_mainpageactions(self):
        self.mp.click_pickupbutton()
        time.sleep(2)
        cl.allurelogs("Clicked on 'Pickup' button")
        self.mp.click_deliverybutton()
        time.sleep(2)
        cl.allurelogs("Clicked on 'Delivery' button")
        self.mp.click_locationbutton()
        time.sleep(2)
        cl.allurelogs("Clicked on 'Location' button")