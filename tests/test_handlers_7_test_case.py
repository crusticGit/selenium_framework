from pages.handlers_page import HandlerPage, NewPage


def test_handlers(browser):
    link = 'http://the-internet.herokuapp.com/windows'
    page = HandlerPage(browser)
    browser.get(link)
    page.wait_for_open()

    page.click_button()
    browser.switch_to_window('New Window')
    new_page = NewPage(browser)
    new_page.wait_for_open()

    actual_result = new_page.get_text_on_page()
    expected_result = 'New Window'
    assert actual_result == expected_result, f"Wrong text on new Page. Expected:{expected_result}, actual:{actual_result}"

    actual_result = browser.title
    expected_result = 'New Window'
    assert actual_result == expected_result, f"Wrong title in new Page. Expected:{expected_result}, actual:{actual_result}"

    browser.switch_to_default_window()

    page.click_button()
    browser.switch_to_window('New Window')
    new_page = NewPage(browser)
    new_page.wait_for_open()
    actual_result = new_page.get_text_on_page()
    expected_result = 'New Window'
    assert actual_result == expected_result, f"Wrong text on new Page. Expected:{expected_result}, actual:{actual_result}"

    actual_result = browser.title
    expected_result = 'New Window'
    assert actual_result == expected_result, f"Wrong title in new Page. Expected:{expected_result}, actual:{actual_result}"

    browser.switch_to_default_window()

    browser.switch_to_window('New Window')
    browser.close()
    browser.switch_to_window('New Window')
    browser.close()
