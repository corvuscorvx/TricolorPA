import allure
from selenium.webdriver.common.by import By

from core.browser import Browser


class ChatWidget:
    CHAT_BODY = (By.CSS_SELECTOR, 'div.chat-body')
    CHAT_FIELD = (By.CSS_SELECTOR, '#chat-widget .chat-footer textarea')
    CHAT_WINDOW = (By.CSS_SELECTOR, '.chat-window')
    CHAT_BUTTON = (By.CSS_SELECTOR, 'div.chat-btn')
    CHAT_SEND_BUTTON = (By.CSS_SELECTOR, 'button.send-btn')
    CHAT_DOWN_BUTTON = (By.CSS_SELECTOR, '#chat-widget .chat-header button.centered')

    def __init__(self, browser: Browser):
        self.browser = browser

    @allure.step('Открыть чат')
    def open(self) -> None:
        self.browser.click_element(self.CHAT_BUTTON)

    @allure.step('Написать сообщение')
    def print_message(self, text: str) -> None:
        self.browser.wait_for_element_visible(self.CHAT_WINDOW)
        self.browser.send_keys_to_element(self.CHAT_FIELD, text)

    @allure.step('Отправить сообщение')
    def send_message(self):
        self.browser.click_element(self.CHAT_SEND_BUTTON)

    @allure.step('Получить текст сообщения из чата')
    def get_current_message(self) -> str:
        return self.browser.get_text(self.CHAT_BODY)

    @allure.step('Получить текст из поля ввода')
    def get_message_in_filed(self):
        element = self.browser.wait_for_element_visible(self.CHAT_FIELD)
        return element.get_attribute("value")

    @allure.step('Свернуть виджет')
    def cut_down_widget(self):
        self.browser.click_element(self.CHAT_DOWN_BUTTON)
        self.browser.wait_for_element_invisible(self.CHAT_WINDOW)

# TODO: прикрепить файл, закрыть
