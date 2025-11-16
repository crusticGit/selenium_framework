import os.path
import random
import tempfile

import pytest
from faker import Faker

from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from logger.logger import Logger


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
    formats = ['.txt', '.html', '.json', '.csv', '.docx']
    file_format = random.choice(formats)
    with tempfile.NamedTemporaryFile(mode='w', suffix=file_format, delete=False) as temp_file:
        Logger.info(f"Create tempfile for test : {temp_file}")
        temp_file.write(Faker().text())
        file_path = temp_file.name

    yield file_path

    if os.path.exists(file_path):
        Logger.info(f"Delete tempfile: {file_path}")
        os.unlink(file_path)
