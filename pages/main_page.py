import allure
from selenium.webdriver.common.by import By

from core.browser import Browser
from pages.components.chat_widget import ChatWidget
from pages.components.geo_window import GeoPopup
from pages.components.search_in_header import SearchInHeader


class MainPage:
    COOKIES_POPUP = (By.CSS_SELECTOR, '.cookie-popup__container')
    COOKIES_POPUP_BUTTON = (By.CSS_SELECTOR, 'a.js--cookie-success')

    HELP_BUTTON_HEADER = (By.CSS_SELECTOR, 'a[href="/help/?section=header"]')

    FIELD_ID = (By.CSS_SELECTOR, '[data-id="check"] input[name="id"]')
    ERROR_AREA = (By.CSS_SELECTOR, '[data-id="check"] .form-item__error')
    CHECK_BUTTON = (By.CSS_SELECTOR, '[data-id="check"] button[type="submit"]')
    CHECK_ID_AREA = (By.CSS_SELECTOR, 'div.main-check-id-form')
    CHECKING_SUBSCRIPTION_BUTTON = (By.CSS_SELECTOR, 'a[href="#check"]')

    ONLINE_CINEMA_BUTTON = (By.CSS_SELECTOR, '.header ._online-kino a')

    def __init__(self, browser: Browser):
        self.browser = browser
        self.chat_widget = ChatWidget(browser)
        self.geo_popup = GeoPopup(browser)
        self.search_in_header = SearchInHeader(browser)

    @allure.step('Принять все куки')
    def accept_cookies(self):
        self.browser.wait_for_element_visible(self.COOKIES_POPUP)
        self.browser.click_element(self.COOKIES_POPUP_BUTTON)

    @allure.step('Открыть страницу "Помощь"')
    def open_the_help_page(self):
        self.browser.click_element(self.HELP_BUTTON_HEADER)

    @allure.step('Написать сообщение в чат')
    def send_message_in_chat(self, message_text: str) -> str:
        self.chat_widget.open()
        self.chat_widget.print_message(message_text)
        self.chat_widget.send_message()
        return self.chat_widget.get_current_message()

    @allure.step('Поиск по сайту из хэдэра')
    def search(self, text: str) -> str:
        self.search_in_header.open()
        self.search_in_header.print_text(text)
        self.search_in_header.click_search_button()
        return self.search_in_header.get_current_search_result()

    @allure.step('Нажать кнопку "Проверить подписки"')
    def click_check_subscription_button(self):
        self.browser.scroll_to_element(self.CHECK_ID_AREA)
        self.browser.click_element(self.CHECKING_SUBSCRIPTION_BUTTON)

    @allure.step('Ввести значение {number_id} в поле')
    def input_id(self, number_id: int):
        self.browser.send_keys_to_element(self.FIELD_ID, number_id)

    @allure.step('Нажать кнопку проверки')
    def click_check_button(self):
        self.browser.click_element(self.CHECK_BUTTON)

    @allure.step('Получить текст ошибки проверки id')
    def get_error_invalid_id(self):
        return self.browser.get_text(self.ERROR_AREA)

    @allure.step('Открыть онлайн-кинотеатр')
    def open_online_cinema(self):
        self.browser.click_element(self.ONLINE_CINEMA_BUTTON)

    @allure.step('Ожидание урла онлайн-кинотеатра')
    def wait_for_online_cinema_url(self, url_part):
        self.browser.wait_for_url_in_new_tab(url_part)
