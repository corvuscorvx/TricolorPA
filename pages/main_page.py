import allure
from selenium.webdriver.common.by import By

from core.browser import Browser
from pages.components.chat_widget import ChatWidget
from pages.components.geo_window import GeoPopup
from pages.components.search_in_header import SearchInHeader
from pages.components.header import Header


class MainPage:
    COOKIES_POPUP = (By.CSS_SELECTOR, '.cookie-popup__container')
    COOKIES_POPUP_BUTTON = (By.CSS_SELECTOR, 'a.js--cookie-success')

    FIELD_ID = (By.CSS_SELECTOR, '[data-id="check"] input[name="id"]')
    ERROR_AREA = (By.CSS_SELECTOR, '[data-id="check"] .form-item__error')
    CHECK_BUTTON = (By.CSS_SELECTOR, '[data-id="check"] button[type="submit"]')
    CHECK_ID_AREA = (By.CSS_SELECTOR, 'div.main-check-id-form')
    RESULT_ID_POPUP = (By.XPATH, "//div[contains(@class, 'h2') and text()='Результат проверки']")
    CHECKING_SUBSCRIPTION_BUTTON = (By.CSS_SELECTOR, 'a[href="#check"]')

    def __init__(self, browser: Browser):
        self.browser = browser
        self.chat_widget = ChatWidget(browser)
        self.geo_popup = GeoPopup(browser)
        self.search_in_header = SearchInHeader(browser)
        self.header = Header(browser)

    # TODO: модернизировать работу с поп-апами на куки и гео (ОС в дз про тестовое задание)
    @allure.step('Принять все куки')
    def accept_cookies(self):
        self.browser.wait_for_element_visible(self.COOKIES_POPUP)
        self.browser.click_element(self.COOKIES_POPUP_BUTTON)

    @allure.step('Открыть страницу "Помощь" из хэдэра')
    def open_the_help_page(self):
        self.header.press_help_button()

    @allure.step('Написать сообщение в чат')
    def send_message_in_chat(self, message_text: str) -> str:
        self.chat_widget.open()
        self.chat_widget.print_message(message_text)
        self.chat_widget.send_message()
        return self.chat_widget.get_current_message()

    @allure.step('Поиск по сайту из хэдэра')
    def search(self, text: str) -> None:
        self.header.press_search_button()
        self.search_in_header.print_text(text)
        self.search_in_header.click_search_button()

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

    @allure.step('Получить ошибки проверки id')
    def get_error_invalid_id(self) -> str:
        return self.browser.get_text(self.ERROR_AREA)

    @allure.step('Получить результат проверки подписок')
    def get_id_check_result(self) -> str:
        return self.browser.get_text(self.RESULT_ID_POPUP)

    @allure.step('Открыть онлайн-кинотеатр из хэдэра')
    def open_online_cinema(self):
        self.header.press_online_cinema_button()

    @allure.step('Ожидание урла онлайн-кинотеатра')
    def wait_for_online_cinema_url(self, url_part):
        self.browser.wait_for_url_in_new_tab(url_part)
