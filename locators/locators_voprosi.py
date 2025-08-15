from selenium.webdriver.common.by import By

class LocatorsVoprosi:
    VOPROS_PRICE = (By.ID, 'accordion__heading-0')
    ANSWER_PRICE = (By.CSS_SELECTOR, "#accordion__panel-0 p")
    TEXT_VOPROS_PRICE = "Сколько это стоит? И как оплатить?"
    TEXT_ANSWER_PRICE = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    VOPROS_MORE_SCOOTERS = (By.ID, 'accordion__heading-1')
    ANSWER_MORE_SCOOTERS = (By.CSS_SELECTOR, "#accordion__panel-1 p")
    TEXT_VOPROS_MORE_SCOOTERS = "Хочу сразу несколько самокатов! Так можно?"
    TEXT_ANSWER_MORE_SCOOTERS = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    VOPROS_TIME_RENT = (By.ID, 'accordion__heading-2')
    ANSWER_TIME_RENT = (By.CSS_SELECTOR, "#accordion__panel-2 p")
    TEXT_VOPROS_TIME_RENT = "Как рассчитывается время аренды?"
    TEXT_ANSWER_TIME_RENT = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    VOPROS_TODAY_ORDER = (By.ID, 'accordion__heading-3')
    ANSWER_TODAY_ORDER = (By.CSS_SELECTOR, "#accordion__panel-3 p")
    TEXT_VOPROS_TODAY_ORDER = "Можно ли заказать самокат прямо на сегодня?"
    TEXT_ANSWER_TODAY_ORDER = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    VOPROS_EXTEND_ORDER = (By.ID, 'accordion__heading-4')
    ANSWER_EXTEND_ORDER = (By.CSS_SELECTOR, "#accordion__panel-4 p")
    TEXT_VOPROS_EXTEND_ORDER = "Можно ли продлить заказ или вернуть самокат раньше?"
    TEXT_ANSWER_EXTEND_ORDER = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    VOPROS_CHARGER = (By.ID, 'accordion__heading-5')
    ANSWER_CHARGER = (By.CSS_SELECTOR, "#accordion__panel-5 p")
    TEXT_VOPROS_CHARGER = "Вы привозите зарядку вместе с самокатом?"
    TEXT_ANSWER_CHARGER = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    VOPROS_CANCEL_ORDER = (By.ID, 'accordion__heading-6')
    ANSWER_CANCEL_ORDER = (By.CSS_SELECTOR, "#accordion__panel-6 p")
    TEXT_VOPROS_CANCEL_ORDER = "Можно ли отменить заказ?"
    TEXT_ANSWER_CANCEL_ORDER = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    VOPROS_OUTSIDE_MKAD = (By.ID, 'accordion__heading-7')
    ANSWER_OUTSIDE_MKAD = (By.CSS_SELECTOR, "#accordion__panel-7 p")
    TEXT_VOPROS_OUTSIDE_MKAD = "Я жизу за МКАДом, привезёте?"
    TEXT_ANSWER_OUTSIDE_MKAD = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
