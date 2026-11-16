import allure
from selenium.webdriver.common.by import By

from core.browser import Browser


class SearchInHeader:
    SEARCH_SHADE = (By.CSS_SELECTOR, '.head-search form')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.head-search input[type=text]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.head-search button.btn')

    def __init__(self, browser: Browser):
        self.browser = browser

    @allure.step('Ввести поисковый запрос')
    def input_text(self, text: str) -> None:
        self.browser.wait_for_element_visible(self.SEARCH_SHADE)
        self.browser.send_keys_to_element(self.SEARCH_FIELD, text)

    @allure.step('Нажать кнопку поиска')
    def click_search_button(self) -> None:
        self.browser.click_element(self.SEARCH_BUTTON)
        self.browser.wait_for_element_invisible(self.SEARCH_SHADE)
