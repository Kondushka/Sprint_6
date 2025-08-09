from selenium.webdriver.support import expected_conditions as EC
from locators.locators_button import LocatorsButton
from locators.locators_form import LocatorsInputForm
import allure


class ObjectPageOrder:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait


    @allure.title("Оформляем заказ")
    def click_order_up(self):
        with allure.step("Ожидаем, пока верхняя кнопка 'Заказать' станет видна"):
            element = self.wait.until(EC.visibility_of_element_located(LocatorsButton.BUTTON_ORDER_UP))
            assert element.is_displayed(), 'Кнопка не появилась'

        with allure.step("Кликаем по верхней кнопке 'Заказать'"):
            self.driver.execute_script("arguments[0].click();", element)

    def click_order_down(self):
        with allure.step("Ожидаем, пока нижняя кнопка 'Заказать' станет видна"):
            element = self.wait.until(EC.visibility_of_element_located(LocatorsButton.BUTTON_ORDER_DOWN))
            assert element.is_displayed(), 'Кнопка не появилась'

        with allure.step("Скроллим к нижней кнопке 'Заказать'"):
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        with allure.step("Кликаем по нижней кнопке 'Заказать'"):
            self.driver.execute_script("arguments[0].click();", element)

    @allure.title("Подтверждаем заказ")
    def confirm_order(self):
        with allure.step('Нажимаем кнопку оформленя заказа'):
            push_botton = self.wait.until(EC.element_to_be_clickable(LocatorsButton.BUTTON_ADD_ORDER))  
            push_botton.click()


        with allure.step("Подтверждаем заказ"):
            confirm_button = self.wait.until(EC.element_to_be_clickable(LocatorsButton.BUTTON_CONFIRM_ORDER))
            confirm_button.click()

        with allure.step("Проверяем, что заказ оформлен"):
            check_order = self.wait.until(EC.visibility_of_element_located(LocatorsInputForm.ORDER_DONE))
            assert "Заказ оформлен" in check_order.text, "Текст 'Заказ оформлен' не найден"
            assert "Заказ оформлен" in check_order.text or "Номер заказа" in check_order.text, \
        f"Текст 'Заказ оформлен' не найден. Было: {check_order.text}"