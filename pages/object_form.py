from selenium.webdriver.support import expected_conditions as EC
from locators.locators_button import LocatorsButton
from locators.locators_form import LocatorsInputForm
import allure
from src.urls import Urls
from src.helpers import Generation


class ObjectPageForm:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    @allure.title("Заполняем форму")

    def input_form(self):
        with allure.step("Ожидаем, пока форма станет видна"):
            expected_url = Urls.ORDER_URL
            current_url = self.driver.current_url
            assert expected_url in current_url, f"Ожидался URL {expected_url}, но получен {current_url}"

        with allure.step("Выбираем поле 'Имя'"):
            surname_input = self.wait.until(EC.presence_of_element_located(LocatorsInputForm.FORM_INPUT_NAME))

        with allure.step(f"Вводим имя: {Generation.random_name}"):
            surname_input.send_keys(Generation.random_name)

        with allure.step("Выбираем поле 'Фамилия'"):
            surname_input = self.wait.until(EC.presence_of_element_located(LocatorsInputForm.FORM_INPUT_SURNAME))

        with allure.step(f"Вводим фамилию: {Generation.random_surname}"):
            surname_input.send_keys(Generation.random_surname)

        with allure.step("Выбираем поле 'Адрес'"):
            address_input = self.driver.find_element(*LocatorsInputForm.FORM_INPUT_ADDRESS)

        with allure.step(f"Вводим адрес: {Generation.random_adress}"):
            address_input.send_keys(Generation.random_adress)

        with allure.step("Выбираем поле 'Станция метро'"):
            metro_input = self.driver.find_element(*LocatorsInputForm.FORM_INPUT_METRO)
            metro_input.click()

        with allure.step(f"Выбираем метро из списка: {Generation.random_metro}"):
            choose_metro = self.wait.until(EC.element_to_be_clickable(LocatorsInputForm.CHOOSE_METRO))
            choose_metro.click()


        with allure.step("Выбираем поле 'Телефон"):
            phone_input = self.driver.find_element(*LocatorsInputForm.FORM_INPUT_PHONE)

            
        with allure.step(f"Вводим телефон: {Generation.random_phone}"):
            phone_input.send_keys(Generation.random_phone)

        with allure.step("Нажимаем кнопку 'Далее'"):
            button_next = self.wait.until(EC.element_to_be_clickable(LocatorsButton.BUTTON_NEXT_TO_FORM_ORDER))
            button_next.click()

        with allure.step('Проверяем, что открылся блок "Про аренду"'):
            rent_text = self.driver.find_element(*LocatorsInputForm.FORM_INPUT_RENT_PERIOD)
            assert rent_text.is_displayed(), 'Текста "Про аренду" нет'

        with allure.step('Выбираем поле "Когда привезти самокат"'):
            input_date = self.wait.until(EC.visibility_of_element_located(LocatorsInputForm.FORM_INPUT_DATE))
            input_date.click()

        with allure.step(f"Выбираем дату: {Generation.random_date}"):
            choose_date = self.driver.find_element(*LocatorsInputForm.CHOOSE_DATE)
            choose_date.click()
            assert rent_text.is_displayed(), 'Дата не выбралась'

        with allure.step('Выбираем поле "Срок аренды"'):
            input_rent = self.driver.find_element(*LocatorsInputForm.FORM_INPUT_RENT_PERIOD)
            input_rent.click()

        with allure.step(f'Вводим период аренды: {Generation.random_rent_period}'):
            input_rent = self.driver.find_element(*LocatorsInputForm.CHOOSE_RENT_PERIOD)
            input_rent.click()
            assert rent_text.is_displayed(), 'Срок аренды не выбрался'

        with allure.step("Выбираем поле 'Цвет самоката'"):
            input_color_scooter = self.wait.until(EC.element_to_be_clickable(LocatorsInputForm.FORM_INPUT_COLOR_SCOOTER))
            input_color_scooter.click()


        with allure.step(f"Выбираем цвет самоката: {Generation.random_color}"):
            choose_color_scooter = self.wait.until(EC.element_to_be_clickable(LocatorsInputForm.CHOOSE_COLOR_SCOOTER))
            choose_color_scooter.click()
