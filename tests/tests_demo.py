import time

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
    demo_page.open_search()
    demo_page.search(request)

    actual_result = demo_page.get_current_search_result()
    assert request in actual_result, f"Отображается {request}"