from selenium.webdriver.common.by import By
from src.helpers import Generation

class LocatorsInputForm:

    FORM_INPUT_NAME = (By.XPATH, '//input[@placeholder = "* Имя"]')
    FORM_INPUT_SURNAME = (By.XPATH, '//input[@placeholder = "* Фамилия"]')
    FORM_INPUT_ADDRESS = (By.XPATH, '//input[@placeholder = "* Адрес: куда привезти заказ"]')
    FORM_INPUT_METRO = (By.XPATH, '//input[@placeholder = "* Станция метро"]')
    FORM_INPUT_PHONE = (By.XPATH, '//input[@placeholder = "* Телефон: на него позвонит курьер"]')
    FORM_INPUT_DATE = (By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]')
    FORM_INPUT_RENT_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    FORM_INPUT_COMMENT = (By.XPATH, '//input[@placeholder = "Комментарий для курьера"]')
    FORM_INPUT_COLOR_SCOOTER = (By.CLASS_NAME, 'Order_Title__3EKne')


    CHOOSE_DATE = (By.XPATH, f'//div[contains(@class, "react-datepicker__day") and text()="{Generation.random_date}"]')
    CHOOSE_COLOR_SCOOTER = (By.ID, f'{Generation.random_color}')
    CHOOSE_RENT_PERIOD = (By.XPATH, f'//div[contains(@class, "Dropdown-option") and text()="{Generation.random_rent_period}"]')
    CHOOSE_METRO = (By.XPATH, f'//div[@class="Order_Text__2broi" and text()="{Generation.random_metro}"]')

    NEXT_PAGE_ORDER_FORM_FOR_RENT = (By.CLASS_NAME, 'Order_Header__BZXOb')
    ORDER_DONE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")



    


