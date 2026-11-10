import allure
from pages.browser import Browser
from selenium.webdriver.common.by import By


class GeoWindow(Browser):
    GEO_POPUP_WINDOW = (By.CSS_SELECTOR, '.geo-popup')
    GEO_BUTTON_HEADER = (By.CSS_SELECTOR, 'a[href="#geo-popup"]')
    GEO_POPUP_BLUE_BUTTON = (By.CSS_SELECTOR, 'a.btn._blue')
    GEO_POPUP_WHITE_BUTTON = (By.CSS_SELECTOR, 'a.btn._white_bg[data-popup="init"]')

    @staticmethod
    def _get_district_locator(district_name: str):
        """Локатор округа"""
        return By.XPATH, f"//a[contains(@class, 'js--tabs-link') and text()='{district_name}']"

    @staticmethod
    def _get_region_locator(region_name: str):
        """Локатор области"""
        return By.XPATH, f"//div[contains(@class, 'geo-popup')]//a[text()='{region_name}']"

    @allure.step("Выбрать гео {district_name} {region_name}")
    def select_geo(self, district_name: str, region_name: str):
        self.click_element(self.GEO_POPUP_WHITE_BUTTON)
        self.wait_for_element_visible(self.GEO_POPUP_WINDOW)

        district_locator = self._get_district_locator(district_name)
        district_element = self.wait_for_element_visible(district_locator)
        district_element.click()

        region_locator = self._get_region_locator(region_name)
        self.click_element(region_locator)

        self.wait_for_element_invisible(self.GEO_POPUP_WINDOW)