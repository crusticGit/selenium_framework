import pytest

from pages.basic_auth_page import BasicAuthPage


@pytest.mark.parametrize("user, password", [('admin', 'admin')])
def test_access_basic_auth(browser, user, password):
    link = f'http://{user}:{password}@the-internet.herokuapp.com/basic_auth'
    page = BasicAuthPage(browser)
    browser.get(link)
    page.wait_for_open()

    actual_result = page.get_success_message()
    expected_result = "Congratulations! You must have the proper credentials."

    assert actual_result == expected_result, (f"Not authorized. Expected:{expected_result},"
                                              f"actual:{actual_result}")
