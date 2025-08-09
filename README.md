# Sprint_6

## UI‑тесты для https://qa-scooter.praktikum-services.ru/ на Selenium + pytest с отчётами Allure. Браузер — Firefox.

- Allure: настроен вывод результатов в папку allure_results/ (очищается перед каждым прогоном).
- Посмотреть отчет:
allure serve allure_results

## Что покрывают тесты

Оформление заказа:
- Запускаем сценарий двумя путями — через верхнюю и через нижнюю кнопки «Заказать».
- Заполняем обе части формы: имя, фамилия, адрес, метро, телефон → дата, срок аренды, цвет самоката.
- Проверяем результат: появляется модалка подтверждения и номер заказа — заказ оформлен успешно.

Логотипы:
- Клик по логотипу «Самокат» возвращает на главную.
- Клик по логотипу «Яндекс» открывает новую вкладку; убеждаемся, что URL ведёт на Dzen (dzen.ru).

FAQ — «Вопросы о важном»:
- Скроллим к нужному вопросу, раскрываем аккордеон и сравниваем текст ответа с ожидаемым.

## Струкрутра:

- pytest.ini — конфиг pytest/Allure.
- conftest.py — фикстуры драйвера и ожиданий.
- src/ — urls.py, helpers.py (генерация данных).
- locators/ — локаторы для кнопок/формы/FAQ.
- allure_results/ - отчеты 
- requirements.txt - зависимости
- pages/ — Page Object’ы:
    - object_page.py
    - object_form.py
    - object_order.py
    - object_logo.py
    - object_voprosi.py
- tests/ — тесты:
    - test_order_up.py
    - test_order_down.py
    - test_logo.py
    - test_voprosi.py
