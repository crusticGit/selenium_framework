import time

from pages.dynamic_content_page import DynamicPage


def test_dynamic_content(browser):
    link = 'http://the-internet.herokuapp.com/dynamic_content'
    browser.get(link)
    page = DynamicPage(browser)
    page.wait_for_open()

    end_time = time.time() + 50
    flag = False

    while end_time > time.time():
        urls = page.get_url_all_image()
        unique_urls = list(set(urls))
        flag = len(urls) != len(unique_urls)

        if flag:
            flag = True
            break
        browser.refresh()

    assert flag, "There are no matching images"
