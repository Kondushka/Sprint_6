from selenium.webdriver.common.by import By

class LocatorsVoprosi:
    VOPROS_PRICE = (By.ID, 'accordion__heading-0')
    TEXT_VOPROS_PRICE = "Сколько это стоит? И как оплатить?"

    VOPROS_MORE_SCOOTERS = (By.ID, 'accordion__heading-1')
    TEXT_MORE_SCOOTERS = "Хочу сразу несколько самокатов! Так можно?"

    VOPROS_TIME_RENT = (By.ID, 'accordion__heading-2')
    TEXT_TIME_RENT = "Как рассчитывается время аренды?"

    VOPROS_TODAY_ORDER = (By.ID, 'accordion__heading-3')
    TEXT_TODAY_ORDER = "Можно ли заказать самокат прямо на сегодня?"

    VOPROS_EXTEND_ORDER = (By.ID, 'accordion__heading-4')
    TEXT_EXTEND_ORDER = "Можно ли продлить заказ или вернуть самокат раньше?"

    VOPROS_CHARGER = (By.ID, 'accordion__heading-5')
    TEXT_CHARGER = "Вы привозите зарядку вместе с самокатом?"

    VOPROS_CANCEL_ORDER = (By.ID, 'accordion__heading-6')
    TEXT_CANCEL_ORDER = "Можно ли отменить заказ?"

    VOPROS_OUTSIDE_MKAD = (By.ID, 'accordion__heading-7')
    TEXT_OUTSIDE_MKAD = "Я жизу за МКАДом, привезёте?"
