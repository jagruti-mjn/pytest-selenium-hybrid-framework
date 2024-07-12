import pytest
from selenium import webdriver

from utility import ReadConfiguration


@pytest.fixture()

def setup_teardown(request):

    Browser = ReadConfiguration.read_configuration("basic info", "BROWSER")
    driver=webdriver.Chrome()
    if Browser.__eq__("Chrome"):
        driver = webdriver.Chrome()
    elif Browser.__eq__("Firefox"):
        driver = webdriver.Firefox()
    elif Browser.__eq__("Edge"):
        driver = webdriver.Edge()
    else:
        print("provide valid browser")
    url = ReadConfiguration.read_configuration("basic info", "URL")
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
