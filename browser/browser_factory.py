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
            options = []

        Logger.info(f"Start webdriver '{driver_name}' with options '{options}'")
        if driver_name == AvailableDriverName.CHROME:
            chrome_options = webdriver.ChromeOptions()
            for option in options:
                chrome_options.add_argument(option)

            driver = webdriver.Chrome(options=chrome_options)

        elif driver_name == AvailableDriverName.EDGE:
            edge_options = webdriver.EdgeOptions()
            for option in options:
                edge_options.add_argument(option)

            driver = webdriver.Edge(options=edge_options)

        elif driver_name == AvailableDriverName.FIREFOX:
            firefox_options = webdriver.FirefoxOptions()
            for option in options:
                firefox_options.add_argument(option)

            driver = webdriver.Firefox(options=firefox_options)

        else:
            raise NotImplementedError(f"{driver_name} not implemented")
        return driver
