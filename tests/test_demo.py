import allure
import pytest


def test_change_geo_from_the_popup(main_page):
    district_name = "Северо-запад"
    region_name = "Санкт-Петербург и Ленинградская Область"

    with allure.step("Принять все куки"):
        main_page.accept_cookies()

    with allure.step("Проверка текущего ГЕО"):
        main_page.geo_popup.get_current_geo()

    with allure.step("Изменить ГЕО"):
        main_page.geo_popup.reject_auto_geo()

    with allure.step("Выбор ГЕО"):
        main_page.geo_popup.select_geo(district_name, region_name)

    with allure.step("Проверка выбранного ГЕО"):
        actual_geo = main_page.geo_popup.get_current_geo()
        assert region_name in actual_geo, f"Отображается {region_name}"


def test_change_geo_from_the_header(main_page):
    district_name = "Сибирь"
    region_name = "Байконур"

    with allure.step("Проверка текущего ГЕО"):
        main_page.geo_popup.get_current_geo()

    with allure.step("Подтвердить ГЕО"):
        main_page.geo_popup.confirm_auto_geo()

    with allure.step("Нажать на ГЕО в хэдэре"):
        main_page.geo_popup.open_geo_selection_from_header()

    with allure.step("Выбор ГЕО"):
        main_page.geo_popup.select_geo(district_name, region_name)

    with allure.step("Проверка выбранного ГЕО"):
        actual_geo = main_page.geo_popup.get_current_geo()
        assert region_name in actual_geo, f"Отображается {region_name}"


def test_write_in_the_chat(main_page):
    message = "Это тест."

    with allure.step("Принять все куки"):
        main_page.accept_cookies()

    with allure.step("Открыть страницу 'Помощь'"):
        main_page.open_the_help_page()

    with allure.step("Написать сообщение в чат"):
        main_page.send_message_in_chat(message)

    with allure.step("Отображаение сообщения на экране"):
        actual_message = main_page.chat_widget.get_current_message()
        assert message in actual_message, f"Ожидалось {message}, а отображается {actual_message}"


def test_saving_text_in_field_chat(main_page):
    message = "Должно сохраниться"

    with allure.step("Принять все куки"):
        main_page.accept_cookies()

    with allure.step("Открыть страницу 'Помощь'"):
        main_page.open_the_help_page()

    with allure.step("Написать сообщение в чат"):
        main_page.chat_widget.open()
        main_page.chat_widget.print_message(message)

    with allure.step("Свернуть виджет чата"):
        main_page.chat_widget.cut_down_widget()

    with allure.step("Повторно открыть чат"):
        main_page.chat_widget.open()

    with allure.step("Проверить сохранение текста в поле ввода"):
        actual_message = main_page.chat_widget.get_message_in_filed()
        assert message in actual_message, f"Ожидалось {message}, а отображается {actual_message}"


# TODO: добавить тест на закрытие чата и прикрепление файла

# TODO: добавить параметризацию (цифры, спец.с, поиск не дал результата)
def test_search(main_page):
    text = "кино"

    with allure.step("Закрыть поп-ап ГЕО"):
        main_page.geo_popup.confirm_auto_geo()

    with allure.step("Поиск"):
        main_page.search(text)

    with allure.step("Проверить результат поиска"):
        actual_result = main_page.search_in_header.get_current_search_result()
        assert text in actual_result, f"Отображается {text}"


@pytest.mark.parametrize("number_id, result", [
    ("40044900046148", "Результат проверки"),
    ("12345678912340", "Неверный ID"),
    ("", "Введите ID"),
    ("12345678912", "Неверный ID"),
    ("1234567890123", "Неверный ID")
],
                         ids=["correct_id", "wrong_id", "empty_id", "incorrect_id_11", "incorrect_id_13"])
def test_check_subscriptions_by_id(main_page, number_id, result):
    with allure.step("Принять все куки"):
        main_page.accept_cookies()

    with allure.step("Закрыть поп-ап ГЕО"):
        main_page.geo_popup.confirm_auto_geo()

    with allure.step("Проверить подписки по id"):
        main_page.click_check_subscription_button()
        main_page.input_id(number_id)
        main_page.click_check_button()

    with allure.step("Получить результат проверки подписок"):
        if result == "Результат проверки":
            actual_result = main_page.get_id_check_result()
            assert result in actual_result
        else:
            actual_error = main_page.get_error_invalid_id()
            assert result in actual_error


def test_redirect_to_online_cinema(main_page):
    url_part = "kino.tricolor.ru"

    with allure.step("Перейти в онлайн кинотеатр"):
        main_page.open_online_cinema()
        main_page.wait_for_online_cinema_url(url_part)

    with allure.step("Проверить урл"):
        current_url = main_page.browser.driver.current_url
        assert url_part in current_url, f"Ожидали '{url_part}' в текущем URL, но получили '{current_url}'"
