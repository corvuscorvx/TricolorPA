import allure
from pages.browser import Browser
from selenium.webdriver.common.by import By
from pages.components.chat_widget import ChatWidget
from pages.components.geo_window import GeoWindow


class HomePage(Browser):
    CHAT_FIELD = (By.CSS_SELECTOR, '.chat-footer textarea')
    CHAT_WINDOW = (By.CSS_SELECTOR, '.chat-window')
    CHAT_BUTTON = (By.CSS_SELECTOR, 'div.chat-btn')
    CHAT_SEND_BUTTON = (By.CSS_SELECTOR, 'button.send-btn')

    HELP_BUTTON_HEADER = (By.CSS_SELECTOR, 'a[href="/help/?section=header"]')

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.geo = GeoWindow(browser)
        self.chat = ChatWidget(browser)


    @allure.step('Отправить сообщение в чат')
    def send_message_to_the_support_chat(self, text: str) -> None:
        self.chat.open()
        self.chat.send_message(text)

