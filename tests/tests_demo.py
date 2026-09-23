def test_change_geo(demo_page):
    district_name = "Северо-запад"
    region_name = "Санкт-Петербург и Ленинградская Область"

    demo_page.accept_cookies()
    demo_page.select_geo_location(district_name, region_name)

    actual_geo = demo_page.get_current_geo_text()
    assert region_name in actual_geo, f"Отображается {region_name}"


def test_write_in_the_chat(demo_page):
    message = "Это тест."

    demo_page.accept_cookies()
    demo_page.open_the_help_page()
    demo_page.open_the_chat()
    demo_page.write_message(message)

    actual_message = demo_page.get_current_chat_message()
    assert message in actual_message, f"Отображается {message}"


def test_search(demo_page):
    request = "кино"
    demo_page.close_geo_popup()
    demo_page.open_search()
    demo_page.input_search_field(request)
    demo_page.click_search_button()

    actual_result = demo_page.get_current_search_result()
    assert request in actual_result, f"Отображается {request}"


# def test_open_online_cinema(demo_page):

def test_negative_check_subscriptions_by_id(demo_page):
    number_id = 12345678912340
    error_text = "Неверный ID"
    demo_page.accept_cookies()
    demo_page.close_geo_popup()
    demo_page.click_check_subscription_button()
    demo_page.input_id(number_id)
    demo_page.click_check_button()

    actual_error = demo_page.get_error_invalid_id()
    assert error_text in actual_error


def test_redirect_to_online_cinema(demo_page):
    url_part = "kino.tricolor.ru"
    demo_page.open_online_cinema()
    demo_page.wait_for_online_cinema_url(url_part)

    assert url_part in demo_page.driver.current_url, f"Ожидали '{url_part}' в текущем URL, но получили '{demo_page.driver.current_url}'"
