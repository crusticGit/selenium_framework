from browser.browser import Browser
from elements.label import Label
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from pages.base_page import BasePage


class ScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = '//*[contains(text(), "Infinite Scroll")]'
    INDENT_LOC = '//*[contains(@class, "jscroll-added")][{}]'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'scroll page'
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, 'label infinite scroll')
        self.indents = MultiWebElement(self.browser, self.INDENT_LOC, "indents", timeout=2)

    def scroll_page(self, indent_count) -> None:
        expected_indent = WebElement(self.browser,
                                     self.INDENT_LOC.format(indent_count),
                                     "last_expected_indent", timeout=1)

        while not expected_indent.is_exists():
            last_indent = list(self.indents)[-1]
            last_indent.scroll_to_element()

    def get_count_indents(self) -> int:
        return len(list(self.indents))
