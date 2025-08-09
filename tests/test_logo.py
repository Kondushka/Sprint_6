import allure
from pages.object_logo import ObjectPageLogo
from pages.object_page import ObjectPage


@allure.title("Проверка логотипа 'Самокат'")
def test_logo_scooter(driver, wait):
    page = ObjectPage(driver, wait)
    logo = ObjectPageLogo(driver, wait)
    page.open()
    page.close_cookie()
    logo.click_logo_scooter()


@allure.title("Проверка логотипа 'Яндекс'")
def test_log_yandex(driver, wait):
    page = ObjectPage(driver, wait)
    logo = ObjectPageLogo(driver, wait)
    
    page.open()
    page.close_cookie()
    logo.click_logo_yandex()