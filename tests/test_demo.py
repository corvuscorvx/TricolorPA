import allure
import pytest


@allure.epic("Геолокация")
@allure.feature("Изменение геолокации")
@allure.story("Изменить автоматически найденное гео")
@allure.title("Изменение через поп-ап")
@allure.tag("Positive")
def test_change_geo_from_the_popup(main_page):
    district_name = "Северо-запад"
    region_name = "Мурманская Область"

    with allure.step("Принять все куки"):
        main_page.accept_cookies()

    with allure.step("Проверка текущего ГЕО в хэдэре"):
        auto_geo = main_page.header.get_current_geo()

    with allure.step("Отклонить автоопределнное ГЕО"):
        main_page.geo_popup.reject_auto_geo()

    with allure.step("Выбор ГЕО: {district_name} {region_name}"):
        main_page.geo_popup.select_geo(district_name, region_name)

    with allure.step("Проверка выбранного ГЕО в хэдэре"):
        actual_geo = main_page.header.get_current_geo()
        assert auto_geo != actual_geo and region_name in actual_geo, f"Ожидалось '{region_name}', получилось '{actual_geo}'"


@allure.epic("Геолокация")
@allure.feature("Изменение геолокации")
@allure.story("Изменить ранее подтвержденное гео")
@allure.title("Изменение через кнопку в хэдэре")
@allure.tag("Positive")
def test_change_geo_from_the_header(main_page):
    district_name = "Сибирь"
    region_name = "Байконур"

    with allure.step("Подтвердить автоопределенное ГЕО"):
        main_page.geo_popup.confirm_auto_geo()

    with allure.step("Открыть окно выбора ГЕО из хэдэра"):
        main_page.header.press_geo_button()

    with allure.step("Выбрать ГЕО: {district_name} {region_name}"):
        main_page.geo_popup.select_geo(district_name, region_name)

    with allure.step("Проверить, что в шапке отображается выбранное ГЕО"):
        actual_geo = main_page.header.get_current_geo()
        assert region_name in actual_geo, f"Ожидалось '{region_name}', отображается '{actual_geo}'"


@allure.epic("Чат")
@allure.feature("Отправка сообщений в чат")
@allure.story("Отправить текстовое сообщение")
@allure.title("Отправка валидного сообщения")
@allure.tag("Positive")
@pytest.mark.parametrize("text", [
    "?",
    "12",
    "А" * 1000,
    "G" * 999
],
                         ids=["1_char", "2_chars", "1000_chars", "999_chars"])
def test_write_in_the_chat_positive(main_page, text):
    with allure.step("Принять все куки"):
        main_page.accept_cookies()

    with allure.step('Открыть страницу "Помощь"'):
        main_page.header.press_help_button()

    with allure.step('Открыть чат'):
        main_page.chat_widget.open()

    with allure.step('Отправить сообщение в чат'):
        main_page.chat_widget.input_message(text)
        main_page.chat_widget.send_message()

    with allure.step('Проверить отображаение сообщения в истории чата'):
        actual_message = main_page.chat_widget.get_current_message()
        assert text in actual_message, f"Ожидалось {text}, а отображается {actual_message}"


@allure.epic("Чат")
@allure.feature("Отправка сообщений в чат")
@allure.story("Отправить текстовое сообщение")
@allure.title("Кнопка отправки недоступна если введено более 1000 символов")
@allure.tag("Negative")
def test_write_in_the_chat_negative(main_page):
    text = "y" * 1001

    with allure.step('Принять все куки'):
        main_page.accept_cookies()

    with allure.step('Открыть страницу "Помощь"'):
        main_page.header.press_help_button()

    with allure.step('Открыть чат и ввести текст длиннее 1000 символов'):
        main_page.chat_widget.open()
        main_page.chat_widget.input_message(text)

    with allure.step('Проверить, что кнопка отправки недоступна'):
        assert main_page.chat_widget.is_send_button_disabled(), f"Ожидалось, что кнопка отправки недоступна"


@allure.epic("Чат")
@allure.feature("Черновик сообщения")
@allure.story("Сохранение текста в поле ввода")
@allure.title("Введенный текст сохраняется после сворачивания виджета")
@allure.tag("Positive")
def test_saving_text_in_field_chat(main_page):
    text = "Должно сохраниться"

    with allure.step('Принять все куки'):
        main_page.accept_cookies()

    with allure.step('Открыть страницу "Помощь"'):
        main_page.header.press_help_button()

    with allure.step('Открыть чат'):
        main_page.chat_widget.open()

    with allure.step('Ввести текст'):
        main_page.chat_widget.input_message(text)

    with allure.step('Свернуть виджет чата'):
        main_page.chat_widget.minimize_widget()

    with allure.step('Повторно открыть чат'):
        main_page.chat_widget.open()

    with allure.step('Проверить сохранение текста в поле ввода'):
        actual_message = main_page.chat_widget.get_message_in_field()
        assert text == actual_message, f"Ожидалось {text}, а отображается {actual_message}"


@allure.epic("Чат")
@allure.feature("Отображение виджета")
@allure.story("Закрыть виджет")
@allure.title("Иконка виджета исчезает при нажатии на крестик")
@allure.tag("Positive")
def test_close_chat(main_page):
    with allure.step('Принять все куки'):
        main_page.accept_cookies()

    with allure.step('Открыть страницу "Помощь"'):
        main_page.header.press_help_button()

    with allure.step('Навести курсор и закрыть иконку чата'):
        main_page.chat_widget.hover_chat_button()
        main_page.chat_widget.close()

    with allure.step('Проверка исчезновения иконки чата'):
        assert main_page.chat_widget.is_chat_icon_invisible(), "Ожидалось, что иконка чата не отображается"


# TODO: добавить тест на прикрепление файла


@allure.epic("Поиск")
@allure.feature("Поиск из хэдэра")
@allure.story("По совпадению")
@allure.title("Поиск по валидному запросу '{text}'")
@allure.tag("Positive")
@pytest.mark.parametrize("text", [
    "Kino",
    "17",
    "Кино",
    "КИНО",
    "кино"
],
                         ids=["en", "numbers", "ru_mix_case", "ru_upper_case", "ru_lower_case"])
def test_search_positive(main_page, search_page, text):
    with allure.step('Закрыть поп-ап ГЕО'):
        main_page.geo_popup.confirm_auto_geo()

    with allure.step(f'Поиск по запросу "{text}"'):
        main_page.header.press_search_button()
        main_page.header.search.input_text(text)
        main_page.header.search.click_search_button()

    with allure.step('Проверить наличие результата поиска'):
        assert search_page.get_current_search_result(), f"Ожидались результаты поиска по запросу '{text}'"


@allure.epic("Поиск")
@allure.feature("Поиск из хэдэра")
@allure.story("Не валидный поиск")
@allure.title("Отображение ошибки при запросе '{text}'")
@allure.tag("Negative")
@pytest.mark.parametrize("text, expected_error", [
    ("+", "В поисковой фразе обнаружена ошибка"),
    ("  ", "В поисковой фразе обнаружена ошибка"),
    ("орориьботлрио", "К сожалению, на ваш поисковый запрос ничего не найдено")
],
                         ids=["symbol", "spaces", "non_existent"])
def test_search_negative(main_page, search_page, text, expected_error):
    with allure.step('Закрыть поп-ап ГЕО'):
        main_page.geo_popup.confirm_auto_geo()

    with allure.step(f'Поиск по запросу "{text}"'):
        main_page.header.press_search_button()
        main_page.header.search.input_text(text)
        main_page.header.search.click_search_button()

    with allure.step('Проверить результат поиска'):
        actual_message = search_page.get_current_search_result()
        assert expected_error in actual_message, f"Ожидали сообщение '{expected_error}', но получили: '{actual_message}'"


@allure.epic("Подписки")
@allure.feature("Проверка подписок")
@allure.story("Проверить наличие подписок по id")
@allure.title("Проверка подписок по валидному Триколор ID")
@allure.tag("Positive")
def test_check_subscriptions_by_id(main_page):
    number_id = "40044900046148"
    expected_result = "Результат проверки"

    with allure.step('Принять все куки'):
        main_page.accept_cookies()

    with allure.step('Закрыть поп-ап ГЕО'):
        main_page.geo_popup.confirm_auto_geo()

    with allure.step('Ввести ID "{number_id}" и нажать "Проверить"'):
        main_page.click_check_subscription_button()
        main_page.input_id(number_id)
        main_page.click_check_button()

    with allure.step('Получить результат проверки подписок'):
        actual_result = main_page.get_id_check_result()
        assert expected_result in actual_result, f"Ожидалось '{expected_result}', но получили: '{actual_result}'"


@allure.epic("Подписки")
@allure.feature("Проверка подписок")
@allure.story("Проверить наличие подписок по id")
@allure.title("Проверка подписок по не валидному Триколор ID")
@allure.tag("Negative")
@pytest.mark.parametrize("number_id, expected_error", [
    ("12345678912340", "Неверный ID"),
    ("", "Введите ID"),
    ("12345678912", "Неверный ID"),
    ("1234567890123", "Неверный ID")
],
                         ids=["non_existent_id", "empty_id", "11_digits", "13_digits"])
def test_check_subscriptions_by_id_negative(main_page, number_id, expected_error):
    with allure.step('Принять все куки'):
        main_page.accept_cookies()

    with allure.step('Закрыть поп-ап ГЕО'):
        main_page.geo_popup.confirm_auto_geo()

    with allure.step('Ввести некорректный ID "{number_id}" и нажать "Проверить"'):
        main_page.click_check_subscription_button()
        main_page.input_id(number_id)
        main_page.click_check_button()

    with allure.step('Получить сообщение об ошибке валидации'):
        actual_error = main_page.get_error_invalid_id()
        assert expected_error in actual_error, f"Ожидали сообщение '{expected_error}', но получили: '{actual_error}'"


@allure.epic("Навигация")
@allure.feature("Онлайн-кинотеатр")
@allure.story("Переход в кинотеатр из хэдэра")
@allure.title("Открытие кинотеатра в новой вкладке")
@allure.tag("Positive")
def test_redirect_to_online_cinema(main_page):
    url_part = "kino.tricolor.ru"

    with allure.step('Нажать кнопку онлайн-кинотеатра в хэдэре'):
        main_page.header.press_online_cinema_button()

    with allure.step('Подождать откртие кинотеатра в новой вкладке'):
        main_page.wait_for_new_tab_url(url_part)

    with allure.step('Проверить урл в открывшейся вкладке'):
        current_url = main_page.get_current_url()
        assert url_part in current_url, f"Ожидали '{url_part}' в текущем URL, но получили '{current_url}'"
