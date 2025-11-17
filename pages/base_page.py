from browser.browser import Browser
from elements.base_element import BaseElement
from logger.logger import Logger


class BasePage:
    UNIQUE_ELEMENT_LOC = None  # should be override

    def __init__(self, browser: Browser):
        self.browser = browser
        self.page_name: str = None
        self.unique_element: BaseElement = None

    def wait_for_open(self) -> None:
        Logger.info(f'{self}: wait for open')
        self.unique_element.wait_for_presence()

    def __str__(self):
        return f"{self.__class__.__name__}[{self.page_name}]"

    def __repr__(self):
        return str(self)
