import allure
import pytest
from pages.page_voprosi import PageVoprosi, FAQ



@pytest.mark.parametrize("locator_question,  expected_text_questions, locator_answer, expected_text_answers", FAQ,
    ids=[
        "price_and_payment",
        "more_scooters",
        "rental_time",
        "today_order",
        "extend_order",
        "charger",
        "cancel_order",
        "outside_mkad"
    ])
@allure.title("FAQ: корректность текста вопроса и ответа")
def test_faq_question(driver, locator_question,  expected_text_questions, locator_answer, expected_text_answers):
    page = PageVoprosi(driver)
    page.open()
    page.close_cookie()

    with allure.step("Выбираем вопрос, проверяем текст ответа и вопроса"):    
        page.check_question(locator_question,  expected_text_questions, locator_answer, expected_text_answers)