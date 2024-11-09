import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils import attach


@pytest.fixture(scope="function")
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "125.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
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