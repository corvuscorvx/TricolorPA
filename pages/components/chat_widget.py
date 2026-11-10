import allure
from selenium.webdriver.common.by import By


from pages.browser import Browser

class ChatWidget(Browser):
    CHAT_FIELD = (By.CSS_SELECTOR, '.chat-footer textarea')
    CHAT_WINDOW = (By.CSS_SELECTOR, '.chat-window')
    CHAT_BUTTON = (By.CSS_SELECTOR, 'div.chat-btn')
    CHAT_SEND_BUTTON = (By.CSS_SELECTOR, 'button.send-btn')

    @allure.step('Открыть чат')
    def open(self):
        self.click_element(self.CHAT_BUTTON)

    @allure.step('Написать сообщение в чат')
    def send_message(self, text: str):
        self.wait_for_element_visible(self.CHAT_WINDOW)
        self.send_keys_to_element(self.CHAT_FIELD, text)
        self.click_element(self.CHAT_SEND_BUTTON)

    @allure.step('Получить текст сообщения из чата')
    def get_current_chat_message(self) -> str:
        return self.get_text(self.CHAT_WINDOW)

# TODO: прикрепить файл, свернуть виджет, закрыть 
