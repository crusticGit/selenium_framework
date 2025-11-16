import time

from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from elements.base_element import BaseElement
from logger.logger import Logger


class Browser:
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 120

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.set_page_load_timeout(self.PAGE_LOAD_TIMEOUT)
        self._wait = WebDriverWait(self._driver, timeout=self.DEFAULT_TIMEOUT)
        self.main_handle = None

    @property
    def driver(self) -> WebDriver:
        return self._driver

    @property
    def url(self) -> str:
        return self._driver.current_url

    def title(self) -> str:
        return self._driver.title

    def backward(self) -> None:
        return self._driver.back()

    def forward(self) -> None:
        return self._driver.forward()

    def get(self, url: str) -> None:
        Logger.info(f"{self}: get '{url}'")
        try:
            self._driver.get(url)
        except WebDriverException as err:
            Logger.error(f'{self}:{err}')
            raise
        self.main_handle = self._driver.current_window_handle
        Logger.info(f'{self}: main handle = "{self.main_handle}"')

    def close(self) -> None:
        Logger.info(f"{self}: close window handle = '{self._driver.current_window_handle}'")
        self._driver.close()

    def quit(self) -> None:
        Logger.info(f"{self}: quit")
        try:
            self._driver.quit()
        except WebDriverException as err:
            Logger.error(f'{self}:{err}')
            raise

    def refresh(self) -> None:
        Logger.info(f"{self}: refresh")
        self._driver.refresh()

    def wait_alert_present(self):
        Logger.info(f"{self}: wait alert present")
        return self._wait.until(expected_conditions.alert_is_present())

    def switch_to_alert(self):
        self.wait_alert_present()
        Logger.info(f"{self}: switch to alert")
        return self._driver.switch_to.alert

    def get_alert_text(self):
        alert = self.switch_to_alert()
        Logger.info(f"{self}: get alert text")
        return alert.text

    def accept_alert(self):
        alert = self.switch_to_alert()
        Logger.info(f"{self}: accept alert")
        alert.accept()

    def send_keys_alert(self, text: str):
        alert = self.switch_to_alert()
        Logger.info(f"{self}: send text: '{text}' in alert")
        try:
            alert.send_keys(text)
        except WebDriverException as err:
            Logger.error(f'{self}:{err}')
            raise

    def switch_to_frame(self, frame: BaseElement):
        Logger.info(f"switch to frame - '{frame}'")
        return self._driver.switch_to.frame(frame.wait_for_presence())

    def switch_to_content_default(self):
        Logger.info(f"{self}: switch to default content")
        try:
            self._driver.switch_to.default_content()
        except WebDriverException as err:
            Logger.error(f'{self}:{err}')
            raise

    def execute_script(self, script: str, *args) -> None:
        Logger.info(f"{self}: execute script = '{script}' with args = '{args}")
        try:
            self._driver.execute_script(script, *args)
        except WebDriverException as err:
            Logger.error(f'{self}:{err}')
            raise

    def save_screenshot(self, filename: str) -> None:
        Logger.info(f"{self}: save screenshot in '{filename}")
        self._driver.save_screenshot(filename=filename)

    def switch_to_default_window(self) -> None:
        Logger.info(f"{self}: switch to default window")
        print(self.main_handle)
        try:
            self._driver.switch_to.window(self.main_handle)
        except WebDriverException as err:
            Logger.error(f'{self}:{err}')
            raise

    def switch_to_window(self, title: str) -> None:
        Logger.info(f"{self}: switch to window with title '{title}'")
        end_time = time.time() + self.PAGE_LOAD_TIMEOUT
        while True:
            handles = self._driver.window_handles
            for handle in handles:
                self._driver.switch_to.window(handle)
                if self._driver.title == title:
                    Logger.info(f"{self}:new window handle = '{self._driver.current_window_handle}")
                    return
            if time.time() < end_time:
                time.sleep(1)
            else:
                raise ValueError(f"{self}: window with title {title} wasn't found")

    def __str__(self) -> str:
        return f'{self.__class__.__name__}-[{self._driver.session_id}]'

    def __repr__(self) -> str:
        return str(self)
