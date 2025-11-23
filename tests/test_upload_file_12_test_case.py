import os.path

import pytest

from pages.upload_page import UploadImage


@pytest.mark.skipif(os.path.exists('/.dockerenv'), reason='Test requires GUI, skipping in Docker')
def test_upload_file_and_dialog_window(browser, temp_random_file):
    link = 'https://the-internet.herokuapp.com/upload'
    browser.get(link)
    page = UploadImage(browser)
    page.wait_for_open()

    page.upload_file_using_dialog_window(temp_random_file)
    page.click_on_upload()

    actual_result = page.get_result_upload_file()
    expected_result = 'File Uploaded!'
    assert actual_result == expected_result, (f'File not loaded!.'
                                              f'Expected:{expected_result}, actual: {actual_result}')

    actual_result = page.get_upload_file_name()
    expected_result = os.path.basename(temp_random_file)
    assert actual_result == expected_result, (f'The file name not matches the uploaded file. '
                                              f'Expected: {expected_result}, actual: {actual_result}')
