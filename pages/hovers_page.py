from browser.browser import Browser
from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = '//h3[contains(text(), "Hovers")]'
    AVATAR_ELEMENTS_LOC = '//*[contains(@class, "figure")][{position}]'
    LINK_ELEMENTS_LOC = '//*[contains(@class, "figure")][{position}]//a'
    NAME_ELEMENTS_LOC = '//*[contains(@class, "figure")][{position}]//h5'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Hovers page'
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "h3 hovers")

    def hover_on_avatar(self, position: int):
        locator_avatar = self.AVATAR_ELEMENTS_LOC.format(position=position)
        avatar = WebElement(self.browser, locator_avatar, f'avatar #{position}')
        avatar.move_to()

    def get_name_avatar(self, position: int):
        locator_name = self.NAME_ELEMENTS_LOC.format(position=position)
        name = WebElement(self.browser, locator_name, f'avatar name #{position}')
        return name.get_text()

    def click_on_profile_avatar(self, position: int):
        locator_link = self.LINK_ELEMENTS_LOC.format(position=position)
        link = Button(self.browser, locator_link, f"link avatar #{position}")
        link.click()
