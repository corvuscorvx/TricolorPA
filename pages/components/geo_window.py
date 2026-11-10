import allure
from pages.browser import Browser
from selenium.webdriver.common.by import By


class GeoWindow:
    GEO_POPUP_WINDOW = (By.CSS_SELECTOR, '.geo-popup')
    GEO_BUTTON_HEADER = (By.CSS_SELECTOR, 'a[href="#geo-popup"]')
    GEO_CORRECT_BUTTON = (By.CSS_SELECTOR, 'a.btn._blue')
    GEO_INCORRECT_BUTTON = (By.CSS_SELECTOR, 'a.btn._white_bg[data-popup="init"]')

    def __init__(self, browser: Browser):
        self.browser = browser

    @staticmethod
    def _get_district_locator(district_name: str):
        """Локатор округа"""
        return By.XPATH, f"//a[contains(@class, 'js--tabs-link') and text()='{district_name}']"

    @staticmethod
    def _get_region_locator(region_name: str):
        """Локатор области"""
        return By.XPATH, f"//div[contains(@class, 'geo-popup')]//a[text()='{region_name}']"

    @allure.step("Выбрать гео {district_name} {region_name}")
    def select_geo(self, district_name: str, region_name: str) -> None:
        self.browser.click_element(self.GEO_INCORRECT_BUTTON)
        self.browser.wait_for_element_visible(self.GEO_POPUP_WINDOW)

        district_locator = self._get_district_locator(district_name)
        self.browser.click_element(district_locator)

        region_locator = self._get_region_locator(region_name)
        self.browser.click_element(region_locator)

        self.browser.wait_for_element_invisible(self.GEO_POPUP_WINDOW)