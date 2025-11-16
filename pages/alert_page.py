from browser.browser import Browser
from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class AlertPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@class, 'example')]//h3"
    BTN_ALERT_LOC = "//*[contains(text(), 'Click for JS Alert')]"
    BTN_CONFIRM_LOC = "//*[contains(text(), 'Click for JS Confirm')]"
    BTN_PROMPT_LOC = "//*[contains(text(), 'Click for JS Prompt')]"
    RESULT_MESSAGE_LOC = "result"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Alert page'
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header js alerts")
        self.result_message = Label(browser, self.RESULT_MESSAGE_LOC, "Result message")

    def trigger_alert(self) -> None:
        element = Button(self.browser, self.BTN_ALERT_LOC, "click btn for alert")
        element.click()

    def trigger_prompt(self) -> None:
        element = Button(self.browser, self.BTN_PROMPT_LOC, "click btn for prompt")
        element.click()

    def trigger_confirm(self) -> None:
        element = Button(self.browser, self.BTN_CONFIRM_LOC, "click btn for confirm")
        element.click()

    def trigger_alert_js_click(self) -> None:
        element = Button(self.browser, self.BTN_ALERT_LOC, "click btn for alert")
        element.js_click()

    def trigger_prompt_js_click(self) -> None:
        element = Button(self.browser, self.BTN_PROMPT_LOC, "click btn for prompt")
        element.js_click()

    def trigger_confirm_js_click(self) -> None:
        element = Button(self.browser, self.BTN_CONFIRM_LOC, "click btn for confirm")
        element.js_click()

    def get_result_text(self) -> str:
        return self.result_message.get_text()
