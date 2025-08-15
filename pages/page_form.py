from locators.locators_button import LocatorsButton
from locators.locators_form import LocatorsInputForm
from pages.base_page import BaseDoWithElements
from src.helpers import Generation


class PageForm(BaseDoWithElements):

    def input_form_step_1(self):
        self.input_keys(LocatorsInputForm.FORM_INPUT_NAME, Generation.random_name)
        self.input_keys(LocatorsInputForm.FORM_INPUT_SURNAME, Generation.random_surname)
        self.input_keys(LocatorsInputForm.FORM_INPUT_ADDRESS, Generation.random_adress)
        self.click(LocatorsInputForm.FORM_INPUT_METRO)
        self.click(LocatorsInputForm.CHOOSE_METRO)
        self.input_keys(LocatorsInputForm.FORM_INPUT_PHONE, Generation.random_phone)


    def button_next(self):
        self.click(LocatorsButton.BUTTON_NEXT_TO_FORM_ORDER)
        return self.find_element(LocatorsInputForm.NEXT_PAGE_ORDER_FORM_FOR_RENT)


    def input_form_step_2(self):
        self.click(LocatorsInputForm.FORM_INPUT_DATE)
        self.click(LocatorsInputForm.CHOOSE_DATE)
        self.click(LocatorsInputForm.FORM_INPUT_RENT_PERIOD)
        self.click(LocatorsInputForm.CHOOSE_RENT_PERIOD)
        self.click(LocatorsInputForm.FORM_INPUT_COLOR_SCOOTER)
        self.click(LocatorsInputForm.CHOOSE_COLOR_SCOOTER)
