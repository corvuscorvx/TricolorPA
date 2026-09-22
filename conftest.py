import os
import pytest
from selenium import webdriver
from pages.demo_page import DemoPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def demo_page(driver):
    driver.get("https://www.tricolor.ru/")
    return DemoPage(driver)