import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    COOKIES_POPUP = (By.CSS_SELECTOR, '.cookie-popup__container')
    COOKIES_POPUP_BUTTON = (By.CSS_SELECTOR, 'a.js--cookie-success')

    FIELD_ID = (By.CSS_SELECTOR, '[data-id="check"] input[name="id"]')
    ERROR_AREA = (By.CSS_SELECTOR, '[data-id="check"] .form-item__error')
    CHECK_BUTTON = (By.CSS_SELECTOR, '[data-id="check"] button[type="submit"]')
    CHECK_ID_AREA = (By.CSS_SELECTOR, 'div.main-check-id-form')
    RESULT_ID_POPUP = (By.XPATH, "//div[contains(@class, 'h2') and text()='Результат проверки']")
    CHECKING_SUBSCRIPTION_BUTTON = (By.CSS_SELECTOR, 'a[href="#check"]')


    @allure.step('Принять все куки')
    def accept_cookies(self) -> None:
        self.browser.wait_for_element_visible(self.COOKIES_POPUP)
        self.browser.click_element(self.COOKIES_POPUP_BUTTON)

    @allure.step('Нажать кнопку "Проверить подписки"')
    def click_check_subscription_button(self) -> None:
        self.browser.scroll_to_element(self.CHECK_ID_AREA)
        self.browser.click_element(self.CHECKING_SUBSCRIPTION_BUTTON)

    @allure.step('Ввести значение {number_id} в поле')
    def input_id(self, number_id: int) -> None:
        self.browser.send_keys_to_element(self.FIELD_ID, number_id)

    @allure.step('Нажать кнопку "Проверить"')
    def click_check_button(self) -> None:
        self.browser.click_element(self.CHECK_BUTTON)

    @allure.step('Получить ошибки проверки id')
    def get_error_invalid_id(self) -> str:
        return self.browser.get_text(self.ERROR_AREA)

    @allure.step('Получить результат проверки подписок')
    def get_id_check_result(self) -> str:
        return self.browser.get_text(self.RESULT_ID_POPUP)
