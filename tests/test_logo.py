import allure
from pages.page_logo import PageLogo
from src.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Проверка логотипа 'Самокат'")
def test_logo_scooter(driver):
    page = PageLogo(driver)

    with allure.step(f'Открываем страницу {Urls.HOME_URL}'):
        page.open()

    with allure.step("Закрываем куки"):
        page.close_cookie()

    with allure.step("Нажимаем на логотип самоката"):
        page.click_logo_scooter()

    with allure.step("Проверяем корректность перехода на главную страницу"):
        page.wait().until(EC.url_contains(Urls.HOME_URL))
        expected_url = Urls.HOME_URL
        current_url = driver.current_url
        assert expected_url in current_url, f"Ожидался URL {expected_url}, но получен {current_url}"

    

@allure.title("Проверка логотипа 'Яндекс'")
def test_log_yandex(driver):
    page = PageLogo(driver)
    
    with allure.step(f'Открываем страницу {Urls.HOME_URL}'):
        page.open()

    with allure.step("Закрываем куки"):
        page.close_cookie()

    with allure.step('Нажимаем на логотип Яндекс, ждём появления второй вкладки, переключаемся, проверяем, что URL содержит "dzen.ru"'):
        page.click_logo_yandex()
        assert Urls.DZEN_URL in driver.current_url, f"Ожидался URL с '{Urls.DZEN_URL}', но получен: {driver.current_url}"