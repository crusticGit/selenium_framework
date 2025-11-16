import os
import random
import tempfile
import time

import pyautogui
from faker import Faker

from logger.logger import Logger


class PyAutoGUIUtilities:
    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info("Handle File Dialog for uploading file")
        time.sleep(3)
        Logger.info(f"Write '{file_path}' to search File Dialog field")

        pyautogui.typewrite(file_path)
        Logger.info("Press enter")
        pyautogui.hotkey('enter')
        time.sleep(3)


class FileUtilities:
    @staticmethod
    def create_temp_file(content: str = None, suffix: str = None) -> str:
        if suffix is None:
            formats = ['.txt', '.html', '.json', '.csv', '.docx']
            suffix = random.choice(formats)

        with tempfile.NamedTemporaryFile(mode='w', suffix=suffix, delete=False) as temp_file:
            Logger.info(f"Create tempfile for test : {temp_file}")
            temp_file.write(Faker().text() if content is None else content)
        return temp_file.name

    @staticmethod
    def delete_file(file_path: str) -> None:
        if os.path.exists(file_path):
            Logger.info(f"Delete tempfile: {file_path}")
            os.unlink(file_path)
