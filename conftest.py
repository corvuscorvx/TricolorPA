import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from utils import attach
from core.browser import Browser

from pages.main_page import MainPage
from pages.search_page import SearchPage

load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="Browser to use"
    )
    parser.addoption(
        "--browser_version",
        default="157.0",
        choices=("148.0", "153.0", "156.0", "157.0"),
        help="Browser version to use"
    )
    parser.addoption(
        "--window_size",
        default="1920*1080",
        help="Window size"
    )
    parser.addoption(
        "--base_url",
        default=os.getenv("BASE_URL"),
        help="Base URL of the site under test"
    )


@pytest.fixture(scope="function")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    window_size = request.config.getoption("--window_size")

    options = ChromeOptions()
    width, height = window_size.split("*")
    options.add_argument(f"--window-size={width},{height}")

    selenoid_capabilities = {
        "browserName": browser,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "screenResolution": f"{width}x{height}x24"
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_url = os.getenv("SELENOID_URL")
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_password = os.getenv("SELENOID_PASSWORD")

    command_executor = f"https://{selenoid_login}:{selenoid_password}@{selenoid_url}/wd/hub"

    driver = webdriver.Remote(
        command_executor=command_executor,
        options=options
    )

    driver.set_window_size(int(width), int(height))
    driver.implicitly_wait(5)

    yield driver

    attach.add_screenshot(driver)
    attach.add_page_source(driver)
    attach.add_console_logs(driver)
    attach.add_video(driver)

    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver, base_url):
    driver.get(f"{base_url}")
    browser = Browser(driver)
    return MainPage(browser)

@pytest.fixture(scope="function")
def search_page(driver, base_url):
    driver.get(f"{base_url}search/?q=")
    browser = Browser(driver)
    return SearchPage(browser)


# TODO: добавить фикстуру создания файла для добавления в тестах
