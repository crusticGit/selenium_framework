from pages.context_menu_page import ContextMenuPage


def test_alert_and_context_click(browser):
    link = 'http://the-internet.herokuapp.com/context_menu'
    page = ContextMenuPage(browser)
    browser.get(link)
    page.wait_for_open()

    page.click_menu_element()
    browser.switch_to_alert()
    actual_result = browser.get_alert_text()
    browser.accept_alert()
    
    expected_result = 'You selected a context menu'
    assert actual_result == expected_result, (f"Wrong alert text. Expected:{expected_result},"
                                              f" actual:{actual_result}")
