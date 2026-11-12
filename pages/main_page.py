import allure
from selenium.webdriver.common.by import By

from core.browser import Browser
from pages.components.chat_widget import ChatWidget
from pages.components.geo_window import GeoPopup


class MainPage:
    COOKIES_POPUP = (By.CSS_SELECTOR, '.cookie-popup__container')
    COOKIES_POPUP_BUTTON = (By.CSS_SELECTOR, 'a.js--cookie-success')

    SEARCH_SHADE = (By.CSS_SELECTOR, '.head-search form')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.head-search input[type=text]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.btn')
    SEARCH_RESULT_AREA = (By.CSS_SELECTOR, '.search-page-grid')
    SEARCH_BUTTON_HEADER = (By.CSS_SELECTOR, 'a.header__search')

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
        self.chat_widget.send_message(message_text)
        return self.chat_widget.get_current_message()

    @allure.step('Открыть поле поиска из хэдэра')
    def open_search(self):
        self.browser.click_element(self.SEARCH_BUTTON_HEADER)

    @allure.step('Ввести поискаовый запрос {text}')
    def input_search_field(self, text):
        self.browser.wait_for_element_visible(self.SEARCH_SHADE)
        self.browser.send_keys_to_element(self.SEARCH_FIELD, text)

    @allure.step('Нажать кнопку поиска запроса')
    def click_search_button(self):
        self.browser.click_element(self.SEARCH_BUTTON)
        self.browser.wait_for_element_invisible(self.SEARCH_SHADE)

    @allure.step('Получить текст результатов поиска')
    def get_current_search_result(self):
        return self.browser.get_text(self.SEARCH_RESULT_AREA)

    @allure.step('Нажать кнопку "Проверить подписки"')
    def click_check_subscription_button(self):
        self.browser.scroll_to_element(self.CHECK_ID_AREA)
        self.browser.click_element(self.CHECKING_SUBSCRIPTION_BUTTON)

    @allure.step('Ввести значение {number_id} в поле')
    def input_id(self, number_id: int):
        self.browser.send_keys_to_element(self.FIELD_ID, number_id)

    @allure.step('Нажать кнопку првоерки')
    def click_check_button(self):
        self.browser.click_element(self.CHECK_BUTTON)

    @allure.step('Получить текст ошибки првоерки id')
    def get_error_invalid_id(self):
        return self.browser.get_text(self.ERROR_AREA)

    @allure.step('Открыть онлайн-кинотеатр')
    def open_online_cinema(self):
        self.browser.click_element(self.ONLINE_CINEMA_BUTTON)

    @allure.step('Ожидание урла онлайн-кинотеатра')
    def wait_for_online_cinema_url(self, url_part):
        self.browser.wait_for_url_in_new_tab(url_part)
