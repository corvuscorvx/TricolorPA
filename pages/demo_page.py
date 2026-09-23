from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DemoPage(BasePage):
    COOKIES_POPUP = (By.CSS_SELECTOR, '.cookie-popup__container')
    COOKIES_POPUP_BUTTON = (By.CSS_SELECTOR, 'a.js--cookie-success')

    GEO_POPUP_WINDOW = (By.CSS_SELECTOR, '.geo-popup')
    GEO_BUTTON_HEADER = (By.CSS_SELECTOR, 'a[href="#geo-popup"]')
    GEO_POPUP_BLUE_BUTTON = (By.CSS_SELECTOR, 'a.btn._blue')
    GEO_POPUP_WHITE_BUTTON = (By.CSS_SELECTOR, 'a.btn._white_bg[data-popup="init"]')  # "Нет, сменить"

    CHAT_FIELD = (By.CSS_SELECTOR, '.chat-footer textarea')
    CHAT_WINDOW = (By.CSS_SELECTOR, '.chat-window')
    CHAT_BUTTON = (By.CSS_SELECTOR, 'div.chat-btn')
    CHAT_SEND_BUTTON = (By.CSS_SELECTOR, 'button.send-btn')

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

    def accept_cookies(self):
        self.wait_for_element_visible(self.COOKIES_POPUP)
        self.click_element(self.COOKIES_POPUP_BUTTON)

    @staticmethod
    def _get_district_locator(district_name: str):
        """Локатор округа"""
        return By.XPATH, f"//a[contains(@class, 'js--tabs-link') and text()='{district_name}']"

    @staticmethod
    def _get_region_locator(region_name: str):
        """Локатор области"""
        return By.XPATH, f"//div[contains(@class, 'geo-popup')]//a[text()='{region_name}']"

    def select_geo_location(self, district_name: str, region_name: str):
        """Выбрать гео"""
        self.click_element(self.GEO_POPUP_WHITE_BUTTON)
        self.wait_for_element_visible(self.GEO_POPUP_WINDOW)

        district_locator = self._get_district_locator(district_name)
        district_element = self.wait_for_element_visible(district_locator)
        district_element.click()

        region_locator = self._get_region_locator(region_name)
        self.click_element(region_locator)

        self.wait_for_element_invisible(self.GEO_POPUP_WINDOW)

    def get_current_geo_text(self) -> str:
        """Получить текст гео из хэдэра"""
        return self.get_element_text(self.GEO_BUTTON_HEADER).strip()

    def open_the_help_page(self):
        """Открыть страницу "Помощь" """
        self.click_element(self.HELP_BUTTON_HEADER)

    def open_the_chat(self):
        """Открыть чат"""
        self.click_element(self.CHAT_BUTTON)

    def write_message(self, text: str):
        """Написать сообщение в чат"""
        self.wait_for_element_visible(self.CHAT_WINDOW)
        self.send_keys_to_element(self.CHAT_FIELD, text)
        self.click_element(self.CHAT_SEND_BUTTON)

    def get_current_chat_message(self) -> str:
        """Получить текст сообщения из чата"""
        return self.get_element_text(self.CHAT_WINDOW)

    def close_geo_popup(self):
        """Закрыть попап гео"""
        self.click_element(self.GEO_POPUP_BLUE_BUTTON)

    def open_search(self):
        """Открыть поле поиска из хэдэра"""
        self.click_element(self.SEARCH_BUTTON_HEADER)

    def input_search_field(self, request):
        """Ввести поискаовый запрос"""
        self.wait_for_element_visible(self.SEARCH_SHADE)
        self.send_keys_to_element(self.SEARCH_FIELD, request)

    def click_search_button(self):
        """Нажать кнопку поиска запроса"""
        self.click_element(self.SEARCH_BUTTON)
        self.wait_for_element_invisible(self.SEARCH_SHADE)

    def get_current_search_result(self):
        """Получить текст результатов поиска"""
        return self.get_element_text(self.SEARCH_RESULT_AREA)

    def click_check_subscription_button(self):
        """Нажать кнопку "Проверить подписки" """
        self.scroll_to_element(self.CHECK_ID_AREA)
        self.click_element(self.CHECKING_SUBSCRIPTION_BUTTON)

    def input_id(self, number_id: int):
        """Ввести id для проверки"""
        self.send_keys_to_element(self.FIELD_ID, number_id)

    def click_check_button(self):
        """Нажать кнопку првоерки"""
        self.click_element(self.CHECK_BUTTON)

    def get_error_invalid_id(self):
        """Получить текст ошибки првоерки id"""
        return self.get_element_text(self.ERROR_AREA)

    def open_online_cinema(self):
        """Открыть онлайн-кинотеатр"""
        self.click_element(self.ONLINE_CINEMA_BUTTON)

    def wait_for_online_cinema_url(self, url_part):
        """Ожидание урла онлайн-кинотеатра"""
        self.wait_for_url_contains(url_part)
