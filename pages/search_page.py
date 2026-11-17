import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_RESULT_AREA = (By.CSS_SELECTOR, '.search-page-grid')

    @allure.step('Открыть страницу поиска напрямую')
    def open(self, base_url: str, query: str = "") -> None:
        url = f"{base_url.rstrip('/')}/search/?q={query}"
        self.browser.driver.get(url)

    @allure.step('Получить текст результатов поиска')
    def get_current_search_result(self):
        return self.browser.get_text(self.SEARCH_RESULT_AREA)
