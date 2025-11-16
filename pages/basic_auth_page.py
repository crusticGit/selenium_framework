from browser.browser import Browser
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class BasicAuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//p"
    SUCCESS_AUTH_MESSAGE_LOC = "//*[@id='content']//p"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Basic Authentication page'
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Unique element on basic auth page")
        self.success_label = Label(browser, self.SUCCESS_AUTH_MESSAGE_LOC, "Success auth message label")

    def get_success_message(self) -> str:
        return self.success_label.get_text()
