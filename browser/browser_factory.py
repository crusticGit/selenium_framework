import platform
from enum import StrEnum

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from logger.logger import Logger


class AvailableDriverName(StrEnum):
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    EDGE = 'edge'


class BrowserFactory:
    @staticmethod
    def get_driver(
            driver_name: AvailableDriverName = AvailableDriverName.CHROME,
            options: list[str] = None
    ) -> WebDriver:
        if options is None:
            options = ["--window-size=1920,1080"]

        docker_options = []
        if platform.system() == 'Linux':
            docker_options = [
                "--headless=new",
                "--user-data-dir=/tmp/chrome-profile",  # Указывает Chrome где хранить пользовательские данные
                "--no-sandbox",  # Без sandbox
                "--disable-dev-shm-usage",  # Без shared memory
                "--disable-gpu"  # Без GPU ускорения
            ]
        all_options = options + docker_options

        Logger.info(f"Start webdriver '{driver_name}' with options '{all_options}'")
        if driver_name == AvailableDriverName.CHROME:
            chrome_options = webdriver.ChromeOptions()
            for option in all_options:
                chrome_options.add_argument(option)

            driver = webdriver.Chrome(options=chrome_options)

        elif driver_name == AvailableDriverName.EDGE:
            edge_options = webdriver.EdgeOptions()
            for option in all_options:
                edge_options.add_argument(option)

            driver = webdriver.Edge(options=edge_options)

        elif driver_name == AvailableDriverName.FIREFOX:
            firefox_options = webdriver.FirefoxOptions()
            for option in all_options:
                firefox_options.add_argument(option)

            driver = webdriver.Firefox(options=firefox_options)

        else:
            raise NotImplementedError(f"{driver_name} not implemented")
        return driver
