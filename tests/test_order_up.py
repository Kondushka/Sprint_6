import allure
from pages.object_page import ObjectPage
from pages.object_form import ObjectPageForm
from pages.object_order import ObjectPageOrder


@allure.title("Позитивный сценарий: оформление заказа через верхнюю кнопку 'Заказать'")
def test_pozitiv_order_up(driver, wait):
    page = ObjectPage(driver, wait)
    form_page = ObjectPageForm(driver, wait)
    order_add = ObjectPageOrder(driver, wait)

    page.open()
    page.close_cookie()
    order_add.click_order_up()
    form_page.input_form()
    order_add.confirm_order()
