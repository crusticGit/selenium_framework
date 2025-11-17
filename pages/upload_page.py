from browser.browser import Browser
from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage
from utils.pyautogui_utils import PyAutoGUIUtilities


class UploadImage(BasePage):
    UNIQUE_ELEMENT_LOC = '//*[contains(text(),"File Uploader")]'

    BTN_UPLOAD_LOC = 'file-submit'
    INPUT_FILE_UPLOAD_lOC = 'file-upload'

    SUCCESS_MESSAGE_UPLOAD_FILE_LOC = '//*[contains(text(), "File Uploaded!")]'
    UPLOADED_FILE_NAME_LOC = 'uploaded-files'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "upload page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "label file uploader")

        self.btn_upload = Button(browser, self.BTN_UPLOAD_LOC, "btn for upload file")
        self.result_upload = Label(browser, self.SUCCESS_MESSAGE_UPLOAD_FILE_LOC, "result upload file")
        self.input_file_upload = Input(browser, self.INPUT_FILE_UPLOAD_lOC, 'input file upload')
        self.uploaded_file = WebElement(browser, self.UPLOADED_FILE_NAME_LOC, 'uploaded file name')

    def click_on_upload(self):
        self.btn_upload.js_click()

    def get_result_upload_file(self) -> str:
        return self.result_upload.get_text()

    def upload_file_using_send_keys(self, file_path: str):
        self.input_file_upload.send_keys(file_path, clear=False)

    def get_upload_file_name(self) -> str:
        return self.uploaded_file.get_text()

    def open_dialog_window(self) -> None:
        self.input_file_upload.action_chains_click()

    def upload_file_using_dialog_window(self, file_path: str):
        self.open_dialog_window()
        PyAutoGUIUtilities.upload_file(file_path)
