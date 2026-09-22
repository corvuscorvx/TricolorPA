from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DemoPage(BasePage):

    GEO_BUTTON = (By.CSS_SELECTOR, 'a[href="#geo-popup"]')
    HELP_BUTTON = (By.CSS_SELECTOR, 'a[href="/help/?section=header"]')
    COOKIES_POPUP = (By.CSS_SELECTOR, '.cookie-popup__container')
    COOKIES_BUTTON = (By.CSS_SELECTOR, 'a.js--cookie-success')
    GEO_POPUP_WINDOW = (By.CSS_SELECTOR, '.geo-popup')
    GEO_CHANGE_BUTTON = (By.CSS_SELECTOR, 'a.btn._white_bg[data-popup="init"]') #"Нет, сменить"
    GEO_BLUE_BUTTON = (By.CSS_SELECTOR, 'a.btn._blue')
    CHAT_BUTTON = (By.CSS_SELECTOR, 'div.chat-btn')
    CHAT_WINDOW = (By.CSS_SELECTOR, '.chat-window')
    CHAT_FIELD = (By.CSS_SELECTOR, '.chat-footer textarea')
    CHAT_SEND_BUTTON = (By.CSS_SELECTOR, 'button.send-btn')
    SEARCH_BUTTON_HEADER = (By.CSS_SELECTOR, 'a.header__search')
    SEARCH_SHADE = (By.CSS_SELECTOR, '.head-search form')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.head-search input[type=text]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.btn')
    SEARCH_RESULT_AREA = (By.CSS_SELECTOR, '.search-page-grid')



    def accept_cookies(self):
        self.wait_for_element_visible(self.COOKIES_POPUP)
        self.click_element(self.COOKIES_BUTTON)

    @staticmethod
    def _get_district_locator(district_name: str):
        """Локатор округа"""
        return By.XPATH, f"//a[contains(@class, 'js--tabs-link') and text()='{district_name}']"

    @staticmethod
    def _get_region_locator(region_name: str):
        """Локатор области"""
        return By.XPATH, f"//div[contains(@class, 'geo-popup')]//a[text()='{region_name}']"

    def select_geo_location(self, district_name: str, region_name: str):
        self.click_element(self.GEO_CHANGE_BUTTON)
        self.wait_for_element_visible(self.GEO_POPUP_WINDOW)

        district_locator = self._get_district_locator(district_name)
        district_element = self.wait_for_element_visible(district_locator)
        district_element.click()

        region_locator = self._get_region_locator(region_name)
        self.click_element(region_locator)

        self.wait_for_element_invisible(self.GEO_POPUP_WINDOW)

    def get_current_geo_text(self) -> str:
        return self.get_element_text(self.GEO_BUTTON).strip()

    def open_the_help_page(self):
        self.click_element(self.HELP_BUTTON)

    def open_the_chat(self):
        self.click_element(self.CHAT_BUTTON)

    def write_message(self, text: str):
        self.wait_for_element_visible(self.CHAT_WINDOW)
        self.send_keys_to_element(self.CHAT_FIELD, text)
        self.click_element(self.CHAT_SEND_BUTTON)

    def get_current_chat_message(self) -> str:
        return self.get_element_text(self.CHAT_WINDOW)

    def open_search(self):
        self.click_element(self.GEO_BLUE_BUTTON)
        self.click_element(self.SEARCH_BUTTON_HEADER)

    def search(self, request):
        self.wait_for_element_visible(self.SEARCH_SHADE)
        self.send_keys_to_element(self.SEARCH_FIELD, request)
        self.click_element(self.SEARCH_BUTTON)
        self.wait_for_element_invisible(self.SEARCH_SHADE)

    def get_current_search_result(self):
        return self.get_element_text(self.SEARCH_RESULT_AREA)




