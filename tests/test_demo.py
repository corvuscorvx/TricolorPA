import allure


def test_change_geo(demo_page):
    district_name = "Северо-запад"
    region_name = "Санкт-Петербург и Ленинградская Область"

    with allure.step("Accept all cookies"):
        demo_page.accept_cookies()

    with allure.step("Geolocation selection"):
        demo_page.select_geo_location(district_name, region_name)

    with allure.step("Geolocation check"):
        actual_geo = demo_page.get_current_geo_text()
        assert region_name in actual_geo, f"Отображается {region_name}"


def test_write_in_the_chat(demo_page):
    message = "Это тест."

    with allure.step("Accept all cookies"):
        demo_page.accept_cookies()

    with allure.step("Sending a message to the chat"):
        demo_page.open_the_help_page()
        demo_page.open_the_chat()
        demo_page.write_message(message)

    with allure.step("Displaying message"):
        actual_message = demo_page.get_current_chat_message()
        assert message in actual_message, f"Отображается {message}"


def test_search(demo_page):
    text = "кино"

    with allure.step("Closing the geolocation popup"):
        demo_page.close_geo_popup()

    with allure.step("Search"):
        demo_page.open_search()
        demo_page.input_search_field(text)
        demo_page.click_search_button()

    with allure.step("Checking search results"):
        actual_result = demo_page.get_current_search_result()
        assert text in actual_result, f"Отображается {text}"


def test_negative_check_subscriptions_by_id(demo_page):
    number_id = 12345678912340
    error_text = "Неверный ID"

    with allure.step("Accept all cookies"):
        demo_page.accept_cookies()

    with allure.step("Closing the geolocation popup"):
        demo_page.close_geo_popup()

    with allure.step("Checking subscriptions by id"):
        demo_page.click_check_subscription_button()
        demo_page.input_id(number_id)
        demo_page.click_check_button()

    with allure.step("Check of result"):
        actual_error = demo_page.get_error_invalid_id()
        assert error_text in actual_error


def test_redirect_to_online_cinema(demo_page):
    url_part = "kino.tricolor.ru"

    with allure.step("Go to the online cinema"):
        demo_page.open_online_cinema()
        demo_page.wait_for_online_cinema_url(url_part)

    with allure.step("URL check"):
        assert url_part in demo_page.driver.current_url, f"Ожидали '{url_part}' в текущем URL, но получили '{demo_page.driver.current_url}'"
