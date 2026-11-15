import allure
from selenium.webdriver.common.by import By

from core.browser import Browser

class SearchInHeader:
    SEARCH_SHADE = (By.CSS_SELECTOR, '.head-search form')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.head-search input[type=text]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.btn')
    SEARCH_RESULT_AREA = (By.CSS_SELECTOR, '.search-page-grid')
    SEARCH_BUTTON_HEADER = (By.CSS_SELECTOR, 'a.header__search')

    def __init__(self, browser: Browser):
        self.browser = browser

    @allure.step('Открыть поле поиска из хэдэра')
    def open(self):
        self.browser.click_element(self.SEARCH_BUTTON_HEADER)

    @allure.step('Ввести поисковый запрос {text}')
    def print_text(self, text: str):
        self.browser.wait_for_element_visible(self.SEARCH_SHADE)
        self.browser.send_keys_to_element(self.SEARCH_FIELD, text)

    @allure.step('Нажать кнопку поиска')
    def click_search_button(self):
        self.browser.click_element(self.SEARCH_BUTTON)
        self.browser.wait_for_element_invisible(self.SEARCH_SHADE)

    @allure.step('Получить текст результатов поиска')
    def get_current_search_result(self):
        return self.browser.get_text(self.SEARCH_RESULT_AREA)