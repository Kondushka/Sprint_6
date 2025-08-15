from selenium.webdriver.common.by import By

class LocatorsButton:

    BUTTON_ORDER_UP = (By.CLASS_NAME, 'Button_Button__ra12g')
    BUTTON_ORDER_DOWN = (By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM')

    BUTTON_CLOSE_COOKIE = (By.CLASS_NAME, 'App_CookieButton__3cvqF')
    BUTTON_NEXT_TO_FORM_ORDER = (By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM")]')
    BUTTON_ADD_ORDER = (By.XPATH, '//button[text()="Заказать" and contains(@class, "Button_Middle__1CSJM")]')
    BUTTON_CONFIRM_ORDER = (By.XPATH, '//button[text()="Да" and contains(@class, "Button_Middle__1CSJM")]')
    BUTTON_LOGO_SCOOTER = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    BUTTON_LOGO_YANDEX = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')