from appium import webdriver


class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8'
        desired_caps['deviceName'] = 'Vestel Venus Z20'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['app'] = ('C:/Users/esame/Downloads/takeaway.apk')
        desired_caps['appPackage'] = 'uk.takeaway.android'
        desired_caps['appActivity'] = 'com.takeaway.android.activity.RestaurantListActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        driver.implicitly_wait(30)

        return driver


