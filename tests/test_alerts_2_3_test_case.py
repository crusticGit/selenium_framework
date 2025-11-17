from faker import Faker

from pages.alert_page import AlertPage


def test_alerts(browser):
    link = 'https://the-internet.herokuapp.com/javascript_alerts'
    page = AlertPage(browser)
    browser.get(link)
    page.wait_for_open()

    page.trigger_alert()
    browser.switch_to_alert()
    actual_result = browser.get_alert_text()
    expected_result = 'I am a JS Alert'
    assert actual_result == expected_result, f"Wrong alert text. Expected:{expected_result}, actual:{actual_result}"

    browser.accept_alert()
    actual_result = page.get_result_text()
    expected_result = 'You successfully clicked an alert'
    assert actual_result == expected_result, f"Wrong result. Expected:{expected_result}, actual:{actual_result}"

    page.trigger_confirm()
    browser.switch_to_alert()
    actual_result = browser.get_alert_text()
    expected_result = 'I am a JS Confirm'
    assert actual_result == expected_result, f"Wrong comfirm text. Expected:{expected_result}, actual:{actual_result}"

    browser.accept_alert()
    actual_result = page.get_result_text()
    expected_result = 'You clicked: Ok'
    assert actual_result == expected_result, f"Wrong result. Expected:{expected_result}, actual:{actual_result}"

    page.trigger_prompt()
    browser.switch_to_alert()
    actual_result = browser.get_alert_text()
    expected_result = 'I am a JS prompt'
    assert actual_result == expected_result, f"Wrong prompt text. Expected:{expected_result}, actual:{actual_result}"

    text_from_prompt = Faker().text()
    browser.send_keys_alert(text_from_prompt)
    browser.accept_alert()
    actual_result = page.get_result_text()
    expected_result = f'You entered: {text_from_prompt}'
    assert actual_result == expected_result, f"Wrong result. Expected:{expected_result}, actual:{actual_result}"


def test_js_alerts(browser):
    link = 'https://the-internet.herokuapp.com/javascript_alerts'
    page = AlertPage(browser)
    browser.get(link)
    page.wait_for_open()

    page.trigger_alert_js_click()
    browser.switch_to_alert()
    actual_result = browser.get_alert_text()
    expected_result = 'I am a JS Alert'
    assert actual_result == expected_result, f"Wrong alert text. Expected:{expected_result}, actual:{actual_result}"

    browser.accept_alert()
    actual_result = page.get_result_text()
    expected_result = 'You successfully clicked an alert'
    assert actual_result == expected_result, f"Wrong result. Expected:{expected_result}, actual:{actual_result}"

    page.trigger_confirm_js_click()
    browser.switch_to_alert()
    actual_result = browser.get_alert_text()
    expected_result = 'I am a JS Confirm'
    assert actual_result == expected_result, f"Wrong comfirm text. Expected:{expected_result}, actual:{actual_result}"

    browser.accept_alert()
    actual_result = page.get_result_text()
    expected_result = 'You clicked: Ok'
    assert actual_result == expected_result, f"Wrong result. Expected:{expected_result}, actual:{actual_result}"

    page.trigger_prompt_js_click()
    browser.switch_to_alert()
    actual_result = browser.get_alert_text()
    expected_result = 'I am a JS prompt'
    assert actual_result == expected_result, f"Wrong prompt text. Expected:{expected_result}, actual:{actual_result}"

    text_from_prompt = Faker().text(15)
    browser.send_keys_alert(text_from_prompt)
    browser.accept_alert()
    actual_result = page.get_result_text()
    expected_result = f'You entered: {text_from_prompt}'
    assert actual_result == expected_result, f"Wrong result. Expected:{expected_result}, actual:{actual_result}"