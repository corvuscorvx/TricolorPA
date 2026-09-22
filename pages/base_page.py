from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.default_timeout = 10
        self.wait = WebDriverWait(self.driver, self.default_timeout)

    def wait_for_element_visible(self, locator):
        """Ожидание видимости элемента на странице"""
        return self.wait.until(ec.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        """Ожидание кликабельности элемента"""
        return self.wait.until(ec.element_to_be_clickable(locator))

    def wait_for_element_invisible(self, locator):
        """Ожидание исчезновения элемента с экрана"""
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def click_element(self, locator):
        """Ожидание кликабельности и клик на элемент"""
        element = self.wait_for_element_clickable(locator)
        element.click()

    def send_keys_to_element(self, locator, text):
        """Ожидание видимости, очистка поля, ввод текста"""
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator) -> str:
        """Получение текста элемента"""
        return self.wait_for_element_visible(locator).text
