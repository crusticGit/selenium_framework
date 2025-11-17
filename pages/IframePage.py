from browser.browser import Browser
from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class IframePage(BasePage):
    UNIQUE_ELEMENT_LOC = '//*[contains(@class, "banner-image")]'

    BTN_ALERT_AND_FRAME_LOC = '//*[contains(text(), "Alerts, Frame & Windows")]'
    BTN_NESTED_FRAME_LOC = '//*[@id="item-3"]//span[contains(text(), "Nested Frames")]'
    BTN_FRAME_LOC = '//*[@id="item-2"]//span[contains(text(), "Frames")]'

    PARENT_IFRAME_LOC = 'frame1'
    CHILD_IFRAME_LOC = '//iframe[contains(@srcdoc, "Child")]'
    TEXT_PARENT_IFRAME = '//*[contains(text(),"Parent frame")]'
    TEXT_CHILD_IFRAME = '//*[contains(text(),"Child Iframe")]'

    IFRAME1_ON_FRAMES_PAGE_LOC = 'frame1'
    IFRAME2_ON_FRAMES_PAGE_LOC = 'frame2'
    TEXT_IFRAME1_LOC = 'sampleHeading'
    TEXT_IFRAME2_LOC = 'sampleHeading'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Iframe Page'
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, 'uniq elem')

        self.alert_frame_btn = Button(browser, self.BTN_ALERT_AND_FRAME_LOC, 'btn alerts, frame')
        self.nested_frame_btn = Button(browser, self.BTN_NESTED_FRAME_LOC, 'btn nested frames')
        self.frame_btn = Button(browser, self.BTN_FRAME_LOC, 'btn frames')

        self.iframe_parent = WebElement(browser, self.PARENT_IFRAME_LOC, 'iframe elem (parent)')
        self.text_parent_iframe = Label(browser, self.TEXT_PARENT_IFRAME, 'text parent frame')
        self.iframe_child = WebElement(browser, self.CHILD_IFRAME_LOC, 'iframe elem (child)')
        self.text_child_iframe = Label(browser, self.TEXT_CHILD_IFRAME, 'text child frame')

        self.iframe1 = WebElement(browser, self.IFRAME1_ON_FRAMES_PAGE_LOC, "frame 1 on frames page")
        self.iframe2 = WebElement(browser, self.IFRAME2_ON_FRAMES_PAGE_LOC, "frame 2 on frames page")
        self.text_iframe1 = Label(browser, self.TEXT_IFRAME1_LOC, 'text frame1')
        self.text_iframe2 = Label(browser, self.TEXT_IFRAME2_LOC, 'text frame2')

    def click_btn_alert_and_frame(self) -> None:
        self.alert_frame_btn.click()

    def click_btn_nested_frame(self) -> None:
        self.nested_frame_btn.click()

    def click_btn_frame(self) -> None:
        self.frame_btn.click()

    def get_text_parent_iframe(self) -> str:
        return self.text_parent_iframe.get_text()

    def get_text_child_iframe(self) -> str:
        return self.text_child_iframe.get_text()

    def get_text_iframe1(self) -> str:
        return self.text_iframe1.get_text()

    def get_text_iframe2(self) -> str:
        return self.text_iframe2.get_text()
