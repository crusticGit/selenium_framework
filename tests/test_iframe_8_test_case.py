from pages.IframePage import IframePage


def test_iframe(browser):
    link = 'https://demoqa.com'
    page = IframePage(browser)
    browser.get(link)
    page.wait_for_open()

    page.click_btn_alert_and_frame()
    page.click_btn_nested_frame()

    browser.switch_to_frame(page.iframe_parent)
    actual_result = page.get_text_parent_iframe()
    expected_result = 'Parent frame'
    assert actual_result == expected_result, (f"Wrong text in Parent Frame. Expected:{expected_result},"
                                              f" actual:{actual_result}")

    browser.switch_to_frame(page.iframe_child)
    actual_result = page.get_text_child_iframe()
    expected_result = 'Child Iframe'
    assert actual_result == expected_result, (f"Wrong text in Child Frame. Expected:{expected_result},"
                                              f" actual:{actual_result}")

    browser.switch_to_content_default()
    page.click_btn_frame()

    browser.switch_to_frame(page.iframe1)
    text_iframe1 = page.get_text_iframe1()
    browser.switch_to_content_default()

    browser.switch_to_frame(page.iframe2)
    text_iframe2 = page.get_text_iframe2()
    browser.switch_to_content_default()

    assert text_iframe1 == text_iframe2, (f"Text from frame 1 and frame 2 does not match."
                                          f" {text_iframe1} != {text_iframe2}")
