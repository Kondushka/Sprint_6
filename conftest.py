import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)


