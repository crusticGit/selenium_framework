from browser.browser import Browser
from elements.web_element import WebElement
from pages.base_page import BasePage


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = 'hot-spot'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Context Menu Page'
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "menu")

    def click_uniq_element(self):
        self.unique_element.context_click()
