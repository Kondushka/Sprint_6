
from pages.base_page import BaseDoWithElements
from locators.locators_voprosi import LocatorsVoprosi as L

FAQ = [(L.VOPROS_PRICE, L.TEXT_VOPROS_PRICE, L.ANSWER_PRICE, L.TEXT_ANSWER_PRICE),
        (L.VOPROS_MORE_SCOOTERS, L.TEXT_VOPROS_MORE_SCOOTERS, L.ANSWER_MORE_SCOOTERS, L.TEXT_ANSWER_MORE_SCOOTERS),
        (L.VOPROS_TIME_RENT, L.TEXT_VOPROS_TIME_RENT, L.ANSWER_TIME_RENT, L.TEXT_ANSWER_TIME_RENT),
        (L.VOPROS_TODAY_ORDER, L.TEXT_VOPROS_TODAY_ORDER, L.ANSWER_TODAY_ORDER, L.TEXT_ANSWER_TODAY_ORDER),
        (L.VOPROS_EXTEND_ORDER, L.TEXT_VOPROS_EXTEND_ORDER, L.ANSWER_EXTEND_ORDER, L.TEXT_ANSWER_EXTEND_ORDER),
        (L.VOPROS_CHARGER, L.TEXT_VOPROS_CHARGER, L.ANSWER_CHARGER, L.TEXT_ANSWER_CHARGER),
        (L.VOPROS_CANCEL_ORDER, L.TEXT_VOPROS_CANCEL_ORDER, L.ANSWER_CANCEL_ORDER, L.TEXT_ANSWER_CANCEL_ORDER),
        (L.VOPROS_OUTSIDE_MKAD, L.TEXT_VOPROS_OUTSIDE_MKAD, L.ANSWER_OUTSIDE_MKAD, L.TEXT_ANSWER_OUTSIDE_MKAD)
        ]


class PageVoprosi(BaseDoWithElements):

    def check_question(self, locator_question, expected_text_questions, locator_answer, expected_text_answers):
        question_element = self.wait_visible(locator_question)
        assert question_element.is_displayed(), 'Вопрос не появился'

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question_element)
        self.driver.execute_script("arguments[0].click();", question_element)
        actual_text_questions = question_element.text.strip()
        assert actual_text_questions == expected_text_questions, f"Ожидали: '{expected_text_questions}', получили: '{actual_text_questions }'"
        
        answer_element = self.wait_visible(locator_answer)
        actual_text_answers = answer_element.text.strip()
        assert actual_text_answers == expected_text_answers, f"Ожидали: '{expected_text_answers}', получили: '{actual_text_answers }'"
