from selenium.webdriver.support import expected_conditions as EC
import allure


class ObjectPageVoprosi:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait


    @allure.step("Кликаем по вопросу и проверяем текст")
    def check_question(self, locator_vopros, expected_text):

        with allure.step("Ожидаем, пока вопрос станет видимым"):
            element = self.wait.until(EC.visibility_of_element_located(locator_vopros))
            assert element.is_displayed(), 'Вопрос не появился'

        with allure.step("Скроллим к элементу"):
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        
        with allure.step("Кликаем на вопрос"):
            self.driver.execute_script("arguments[0].click();", element)

        with allure.step("Проверяем текст вопроса"):
            actual_text  = element.text.strip()
            assert actual_text == expected_text, f"Ожидали: '{expected_text}', получили: '{actual_text }'"
