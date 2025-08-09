import allure
from locators.locators_voprosi import LocatorsVoprosi
from pages.object_page import ObjectPage
from pages.object_voprosi import ObjectPageVoprosi


def open_page_and_check_question(driver, wait, locator, expected_text):
    page = ObjectPage(driver, wait)
    page.open()
    page.close_cookie()
    page_voprosi = ObjectPageVoprosi(driver, wait)
    page_voprosi.check_question(locator, expected_text)



def test_price_question(driver, wait):
    allure.dynamic.title(f"Проверка текста вопроса '{LocatorsVoprosi.TEXT_VOPROS_PRICE}'")
    open_page_and_check_question(driver, wait, LocatorsVoprosi.VOPROS_PRICE, LocatorsVoprosi.TEXT_VOPROS_PRICE)



def test_more_scooters_question(driver, wait):
    allure.dynamic.title(f"Проверка текста вопроса '{LocatorsVoprosi.TEXT_MORE_SCOOTERS}'")
    open_page_and_check_question(driver, wait, LocatorsVoprosi.VOPROS_MORE_SCOOTERS, LocatorsVoprosi.TEXT_MORE_SCOOTERS)



def test_time_rent_question(driver, wait):
    allure.dynamic.title(f"Проверка текста вопроса '{LocatorsVoprosi.TEXT_TIME_RENT}'")
    open_page_and_check_question(driver, wait, LocatorsVoprosi.VOPROS_TIME_RENT, LocatorsVoprosi.TEXT_TIME_RENT)



def test_today_order_question(driver, wait):
    allure.dynamic.title(f"Проверка текста вопроса '{LocatorsVoprosi.TEXT_TODAY_ORDER}'")
    open_page_and_check_question(driver, wait, LocatorsVoprosi.VOPROS_TODAY_ORDER, LocatorsVoprosi.TEXT_TODAY_ORDER)



def test_charger_question(driver, wait):
    allure.dynamic.title(f"Проверка текста вопроса '{LocatorsVoprosi.TEXT_CHARGER}'")
    open_page_and_check_question(driver, wait, LocatorsVoprosi.VOPROS_CHARGER, LocatorsVoprosi.TEXT_CHARGER)



def test_cancel_order_question(driver, wait):
    allure.dynamic.title(f"Проверка текста вопроса '{LocatorsVoprosi.TEXT_CANCEL_ORDER}'")
    open_page_and_check_question(driver, wait, LocatorsVoprosi.VOPROS_CANCEL_ORDER, LocatorsVoprosi.TEXT_CANCEL_ORDER)


def test_outside_mkad_question(driver, wait):
    allure.dynamic.title(f"Проверка текста вопроса '{LocatorsVoprosi.TEXT_OUTSIDE_MKAD}'")
    open_page_and_check_question(driver, wait, LocatorsVoprosi.VOPROS_OUTSIDE_MKAD, LocatorsVoprosi.TEXT_OUTSIDE_MKAD)