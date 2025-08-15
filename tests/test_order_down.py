import allure
from pages.page_order import PageOrder
from src.urls import Urls


@allure.title("Позитивный сценарий: оформление заказа через нижнюю кнопку 'Заказать'")

def test_pozitiv_order_up(driver):
    page = PageOrder(driver)

    with allure.step(f'Открываем страницу {Urls.HOME_URL}'):
        page.open()

    with allure.step("Закрываем куки"):
        page.close_cookie()

    with allure.step("Ппроверяем нижнюю кнопку 'Заказать'"):
        page.click_order_down()

    expected_url = Urls.ORDER_URL
    current_url = driver.current_url
    assert expected_url in current_url, f"Ожидался URL {expected_url}, но получен {current_url}"
    
    with allure.step("Заполняем данные: имя, фамилия, адрес, метро, телефон"):
        page.input_form_step_1()

    with allure.step("Нажимаем кнопку 'Далее'"):
        elemet = page.button_next()

    with allure.step('Проверяем, что открылся блок "Про аренду"'):
        assert elemet.is_displayed(), 'Блок про аренду не открылся'
        

    with allure.step("Заполняем данные: дата аренды, срок аренды, цвет самоката"):
        page.input_form_step_2()

    with allure.step("Подтверждаем заказ"):
        check_order = page.confirm_order()
        assert "Заказ оформлен" in check_order.text or "Номер заказа" in check_order.text, \
            f"Текст 'Заказ оформлен' не найден. Было: {check_order.text}"