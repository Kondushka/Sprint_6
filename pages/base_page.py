from src.urls import Urls
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators_button import LocatorsButton


class BasePage:

    def __init__(self, driver):
        self.driver = driver
    

    def wait(self):
        return WebDriverWait(self.driver, 15)


    def open(self): 
        self.driver.get(Urls.HOME_URL)


    def close_cookie(self):
        element = self.wait().until(EC.visibility_of_element_located(LocatorsButton.BUTTON_CLOSE_COOKIE))
        self.driver.execute_script("arguments[0].click();", element)



class BaseDoWithElements(BasePage):

    def wait_presence(self, locator):
        return self.wait().until(EC.presence_of_element_located(locator))


    def wait_visible(self, locator):
        return self.wait().until(EC.visibility_of_element_located(locator))
    

    def wait_clickable(self, locator):
        return self.wait().until(EC.element_to_be_clickable(locator))
        

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    

    def input_keys(self, locator, input_key):
        element = self.wait_visible(locator)
        element.send_keys(input_key)


    def click(self, locator):
        element = self.wait_clickable(locator)
        element.click()
