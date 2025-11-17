from browser.browser import Browser
from elements.label import Label
from elements.multi_web_element import MultiWebElement
from pages.base_page import BasePage


class DynamicPage(BasePage):
    UNIQUE_ELEMENT_LOC = '//*[contains(text(), "Dynamic Content")]'
    IMAGE_LOC = '(//*[@id="content"]//img)[{}]'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "dynamic page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "label dynamic content")
        self.images = MultiWebElement(self.browser, self.IMAGE_LOC, "img element")

    def get_url_all_image(self) -> list:
        return [img.get_attribute("src") for img in self.images]
