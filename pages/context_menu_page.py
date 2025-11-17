from browser.browser import Browser
from elements.web_element import WebElement
from pages.base_page import BasePage


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = 'hot-spot'
    MENU_ELEMENT_lOC = UNIQUE_ELEMENT_LOC

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Context Menu Page'
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "uniq elem")
        self.menu_element = WebElement(browser, self.MENU_ELEMENT_lOC, "menu elem")

    def click_menu_element(self):
        self.menu_element.context_click()
