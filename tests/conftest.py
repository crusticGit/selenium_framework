import pytest

from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from logger.logger import Logger
from utils.pyautogui_utils import FileUtilities


@pytest.fixture(scope="function")
def browser():
    Logger.info("Browser start")
    driver = BrowserFactory.get_driver(
        driver_name=AvailableDriverName.CHROME
    )
    browser = Browser(driver)
    yield browser
    browser.quit()
    Logger.info("Browser end")


@pytest.fixture(scope="function")
def temp_random_file():
    file_path = FileUtilities.create_temp_file()
    yield file_path
    FileUtilities.delete_file(file_path)
