import pytest
import time
from APP_testdemo.Driver.Driver import Driver


@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver = Driver()
    driver = driver.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')

@pytest.yield_fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')