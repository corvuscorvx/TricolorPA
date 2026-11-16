import allure
from selenium.webdriver.common.by import By

from core.browser import Browser
from pages.components.search_in_header import SearchInHeader

class SearchPage:
    SEARCH_RESULT_AREA = (By.CSS_SELECTOR, '.search-page-grid')

    def __init__(self, browser: Browser):
        self.browser = browser
        self.search_in_header = SearchInHeader(browser)

    @allure.step('Получить текст результатов поиска')
    def get_current_search_result(self):
        return self.browser.get_text(self.SEARCH_RESULT_AREA)