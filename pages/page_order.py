from locators.locators_button import LocatorsButton
from locators.locators_form import LocatorsInputForm
from pages.page_form import PageForm


class PageOrder(PageForm):

    def click_order_up(self):
        return self.click(LocatorsButton.BUTTON_ORDER_UP)


    def click_order_down(self):
        element = self.wait_visible(LocatorsButton.BUTTON_ORDER_DOWN)
        assert element.is_displayed(), 'Кнопка не появилась'

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    
    def confirm_order(self):
        self.click(LocatorsButton.BUTTON_ADD_ORDER)
        self.click(LocatorsButton.BUTTON_CONFIRM_ORDER)
        return self.wait_visible(LocatorsInputForm.ORDER_DONE)
        
        