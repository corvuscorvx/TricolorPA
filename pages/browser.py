from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Browser:

    def __init__(self, driver: WebDriver, default_timeout: int = 10):
        self.driver = driver
        self.default_timeout = default_timeout
        self.wait = WebDriverWait(driver, default_timeout)

    def wait_for_element_visible(self, locator: Tuple[str, str]):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator: Tuple[str, str]):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def wait_for_element_invisible(self, locator: Tuple[str, str]):
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def click_element(self, locator: Tuple[str, str]) -> None:
        element = self.wait_for_element_clickable(locator)
        element.click()

    def send_keys_to_element(self, locator, text: str | int) -> None:
        text_to_send = str(text)
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text_to_send)

    def get_text(self, locator: Tuple[str, str]) -> str:
        element = self.wait_for_element_visible(locator)
        return element.text

    def scroll_to_element(self, locator: Tuple[str, str]):
        element = self.wait.until(ec.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def wait_for_url_in_new_tab(self, url_part: str) -> bool:
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        return bool(self.wait.until(ec.url_contains(url_part)))
