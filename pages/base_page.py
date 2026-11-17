import allure

from core.browser import Browser
from pages.components.header import Header
from pages.components.geo_popup import GeoPopup
from pages.components.chat_widget import ChatWidget


class BasePage:
    def __init__(self, browser: Browser):
        self.browser = browser
        self.header = Header(browser)
        self.geo_popup = GeoPopup(browser)
        self.chat_widget = ChatWidget(browser)

    @allure.step("Ожидание открытия новой вкладки с URL, содержащим '{url_part}'")
    def wait_for_new_tab_url(self, url_part: str) -> None:
        self.browser.wait_for_url_in_new_tab(url_part)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self) -> str:
        return self.browser.get_current_url()
