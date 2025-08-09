from selenium.webdriver.support import expected_conditions as EC
from locators.locators_button import LocatorsButton
import allure
from src.urls import Urls


class ObjectPageLogo:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    @allure.title("Проверяем логотип 'Скутер'")
    def click_logo_scooter(self):
        with allure.step("Нажимаем на логотип самоката"):
            button_logo_scooter = self.driver.find_element(*LocatorsButton.BUTTON_LOGO_SCOOTER)
            button_logo_scooter.click()

        with allure.step(f"Проверяем корректность перехода на главную страницу {Urls.HOME_URL}"):
            expected_url = Urls.HOME_URL
            current_url = self.driver.current_url
            assert expected_url in current_url, f"Ожидался URL {expected_url}, но получен {current_url}"

    @allure.title("Проверяем логотип 'Яндекс'")
    def click_logo_yandex(self):
        with allure.step("Нажимаем на логотип Яндекс"):
            button_logo_yandex = self.driver.find_element(*LocatorsButton.BUTTON_LOGO_YANDEX)
            button_logo_yandex.click()

        with allure.step("Ждём появления второй вкладки"):
            self.wait.until(EC.number_of_windows_to_be(2))

        with allure.step("Переключаемся на новую вкладку"):
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[1])

        with allure.step("Ждём, пока откроется страница Дзена"):
            self.wait.until(lambda d: d.current_url != "about:blank")

        with allure.step(f"Проверяем, что URL содержит {Urls.DZEN_URL}"):   
            assert Urls.DZEN_URL in self.driver.current_url, f"Ожидался URL с '{Urls.DZEN_URL}', но получен: {self.driver.current_url}"