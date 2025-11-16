import random

from pages.horizontal_slider_page import HorizontalSliderPage


def test_install_value_for_horizontal_slider(browser):
    link = 'https://the-internet.herokuapp.com/horizontal_slider'
    page = HorizontalSliderPage(browser)
    browser.get(link)
    page.wait_for_open()

    max_value = page.get_max_value_slider()
    min_value = page.get_min_value_slider()
    step = page.slider_step()
    steps = int((max_value - min_value) / step) + 1

    list_slider_value = [min_value + i*step for i in range(1, steps-1)]
    random_slider_value = random.choice(list_slider_value)
    page.install_slider_value(random_slider_value)

    actual_result = page.get_slider_value()
    assert actual_result == random_slider_value, (f"Wrong slider value. Expected:{random_slider_value},"
                                                  f" actual:{actual_result}")
