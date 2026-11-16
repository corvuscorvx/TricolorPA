import allure
from selenium.webdriver.common.by import By

from core.browser import Browser
from pages.components.search_in_header import SearchInHeader


class Header:
    GEO_BUTTON_HEADER = (By.CSS_SELECTOR, 'a[href="#geo-popup"]')
    GEO_SELECT_WINDOW = (By.CSS_SELECTOR, '.geo-popup')
    HELP_BUTTON_HEADER = (By.CSS_SELECTOR, 'a[href="/help/?section=header"]')
    ONLINE_CINEMA_BUTTON = (By.CSS_SELECTOR, '.header ._online-kino a')
    SEARCH_BUTTON_HEADER = (By.CSS_SELECTOR, 'a.header__search')

    def __init__(self, browser: Browser):
        self.browser = browser
        self.search = SearchInHeader(browser)

    @allure.step('Нажать кнопку "Помощь"')
    def press_help_button(self) -> None:
        self.browser.click_element(self.HELP_BUTTON_HEADER)

    @allure.step('Нажать кнопку "Онлайн-кинотеатр"')
    def press_online_cinema_button(self) -> None:
        self.browser.click_element(self.ONLINE_CINEMA_BUTTON)

    @allure.step('Нажать кнопку "Поиск"')
    def press_search_button(self) -> None:
        self.browser.click_element(self.SEARCH_BUTTON_HEADER)

    @allure.step('Нажать кнопку "ГЕО" из хэдэра')
    def press_geo_button(self) -> None:
        self.browser.click_element(self.GEO_BUTTON_HEADER)
        self.browser.wait_for_element_visible(self.GEO_SELECT_WINDOW)

    @allure.step('Получить значение текущего ГЕО  из хэдэра')
    def get_current_geo(self) -> str:
        return self.browser.get_text(self.GEO_BUTTON_HEADER).strip()
