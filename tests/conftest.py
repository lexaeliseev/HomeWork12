import os

import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils import attach
from dotenv import load_dotenv

DEFAULT_BROWSER_VERSION = '125.0'


def pytest_addoption(parser):
    """ Если указать перечень для выбора """
    parser.addoption(
        '--browser_version',
        help='Версия браузера в которой будут запущены тесты',
        choices=['100.0', '120.0', '125.0']
    )

    # """ Просто указать параметр для параметризации """
    # parser.addoption('--browser_version'
    #                  )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def setup_browser(request):
    chrome_version = request.config.getoption('--browser_version')
    chrome_version = chrome_version if chrome_version != '' else DEFAULT_BROWSER_VERSION

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": chrome_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    selenoid_login = os.getenv('LOGIN')
    selenoid_password = os.getenv('PASSWORD')
    selenoid_url = os.getenv("SELENOID_ULR")
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_password}@{selenoid_url}",
        options=options)

    browser.config.driver = driver

    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://demoqa.com'

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()