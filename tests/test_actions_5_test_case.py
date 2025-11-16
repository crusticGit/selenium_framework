import pytest

from pages.horizontal_slider_page import HorizontalSliderPage


@pytest.mark.parametrize('slider_value', [3.5])
def test_install_value_for_horizontal_slider(browser, slider_value):
    link = 'https://the-internet.herokuapp.com/horizontal_slider'
    page = HorizontalSliderPage(browser)
    browser.get(link)
    page.wait_for_open()

    page.install_slider_value(slider_value)

    actual_result = page.get_slider_value()
    expected_result = slider_value
    assert actual_result == expected_result, (f"Wrong slider value. Expected:{expected_result},"
                                              f" actual:{actual_result}")
