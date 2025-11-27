import platform
import time

if platform.system() != 'Linux':
    import pyautogui

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
