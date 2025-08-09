from selenium.webdriver.support import expected_conditions as EC
from locators.locators_button import LocatorsButton
import allure
from src.urls import Urls


class ObjectPage:

    @allure.description('Открываем браузер')
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait


    @allure.step(f'Открываем страницу {Urls.HOME_URL}')
    def open(self): 
        self.driver.get(Urls.HOME_URL)


    @allure.step("Закрываем куки")
    def close_cookie(self):
        with allure.step("Ожидаем, пока кнопка станет видна"):
            element = self.wait.until(EC.visibility_of_element_located(LocatorsButton.BUTTON_CLOSE_COOKIE))
            assert element.is_displayed(), 'Кнопка не появилась'
        
        with allure.step("Кликаем по кнопке"):
            self.driver.execute_script("arguments[0].click();", element)
