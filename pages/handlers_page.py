from browser.browser import Browser
from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class NewPage(BasePage):
    UNIQUE_ELEMENT_LOC = '//h3[contains(text(),"New Window")]'
    TEXT_ELEMENT_LOC = '//h3[contains(text(),"New Window")]'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'new page'
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, 'Label new window')
        self.text_elem = Label(browser, self.UNIQUE_ELEMENT_LOC, 'text new window')

    def get_text_on_page(self):
        return self.text_elem.get_text()


class HandlerPage(BasePage):
    UNIQUE_ELEMENT_LOC = '//h3[contains(text(),"Opening")]'
    BUTTON_LOC = '//a[contains(@href, "windows/new")]'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'handlers page'
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, 'Label opening new window')
        self.button_to_open_new_window = Button(browser, self.BUTTON_LOC, 'button for open new window')

    def click_button(self):
        self.button_to_open_new_window.click()
