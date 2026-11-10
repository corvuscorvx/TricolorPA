import allure
from pages.browser import Browser
from selenium.webdriver.common.by import By


class HomePage(Browser):
    CHAT_FIELD = (By.CSS_SELECTOR, '.chat-footer textarea')
    CHAT_WINDOW = (By.CSS_SELECTOR, '.chat-window')
    CHAT_BUTTON = (By.CSS_SELECTOR, 'div.chat-btn')
    CHAT_SEND_BUTTON = (By.CSS_SELECTOR, 'button.send-btn')

    HELP_BUTTON_HEADER = (By.CSS_SELECTOR, 'a[href="/help/?section=header"]')


    @allure.step('Открыть страницу "Помощь"')
    def open_the_help_page(self):
        self.click_element(self.HELP_BUTTON_HEADER)

