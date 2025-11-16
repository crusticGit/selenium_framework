from selenium.webdriver import Keys

from browser.browser import Browser
from elements.web_element import WebElement
from pages.base_page import BasePage


class HorizontalSliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = '//*[contains(@class, "sliderContainer")]//input'
    SLIDER_VALUE_LOC = '//span[@id="range"]'
    SLIDER = UNIQUE_ELEMENT_LOC

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = 'Horizontal slider page'
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, 'uniq element - horizontal slider')
        self.slider_value = WebElement(browser, self.SLIDER_VALUE_LOC, 'slider value')
        self.slider = WebElement(browser, self.SLIDER, 'horizontal slider')

    def get_slider_value(self) -> float:
        return float(self.slider_value.get_text())

    def slider_step(self) -> float:
        return float(self.slider.get_attribute('step'))

    def install_slider_value(self, value: float) -> None:
        last_value = self.get_slider_value()
        next_value = value
        count_step = (next_value - last_value) / self.slider_step()

        for i in range(int(abs(count_step))):
            self.slider.send_keys(Keys.ARROW_LEFT) if count_step < 0 \
                else self.slider.send_keys(Keys.ARROW_RIGHT)
