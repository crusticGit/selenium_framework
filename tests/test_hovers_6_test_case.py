from pages.hovers_page import HoversPage


def test_hover_effect_for_avatar(browser):
    link = 'https://the-internet.herokuapp.com/hovers'
    page = HoversPage(browser)
    browser.get(link)
    page.wait_for_open()

    for i in range(1, 4):
        page.hover_on_avatar(i)

        actual_result = page.get_name_avatar(i)
        expected_result = "name: user" + str(i)
        assert actual_result == expected_result, (f"Wrong name. Expected:{expected_result},"
                                                  f" actual:{actual_result}")
        page.click_on_profile_avatar(i)
        assert browser.url.endswith(f'/users/{i}'), (f"Wrong url. Expected:{expected_result}, "
                                                     f"actual:{actual_result}")
        browser.back()
