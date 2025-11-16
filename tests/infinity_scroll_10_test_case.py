import pytest

from browser.browser import Browser
from pages.infinite_scroll_page import ScrollPage


@pytest.mark.parametrize("age", [23])
def test_infinity_scroll(browser: Browser, age):
    link = 'http://the-internet.herokuapp.com/infinite_scroll'
    browser.get(link)
    page = ScrollPage(browser)
    page.wait_for_open()

    page.scroll_page(age)
    actual_result = page.get_count_indents()
    assert actual_result == age, (f"Count of indents doesn't match the age. "
                                  f"Expected:{age}, actual:{actual_result}")
