from selenium.webdriver.support import expected_conditions as EC
from locators.locators_button import LocatorsButton
from pages.base_page import BaseDoWithElements
from src.urls import Urls

class PageLogo(BaseDoWithElements):

    def click_logo_scooter(self):
            self.click(LocatorsButton.BUTTON_LOGO_SCOOTER)



    def click_logo_yandex(self):
        self.find_element(LocatorsButton.BUTTON_LOGO_YANDEX).click()
        self.wait().until(EC.number_of_windows_to_be(2))
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        return self.wait().until(EC.url_contains(Urls.DZEN_URL))


