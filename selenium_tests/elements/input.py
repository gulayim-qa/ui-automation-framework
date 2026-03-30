import time
from typing import Optional
from selenium.common.exceptions import WebDriverException
from selenium_tests.elements.base_element import BaseElement
from selenium_tests.utils.logger.logger import Logger

class Input(BaseElement):
    """Input Class-wrapper for Selenium WebElement."""

    def clear(self, timeout: Optional[int] = None) -> None:
        timeout = timeout or self.default_timeout
        element = self.wait_visibility(timeout=timeout)
        Logger.info(f'{self}: clear', to_file=True)

        try:
            element.clear()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            self.driver.dump()
            raise

    def send_keys(
        self, keys: str, timeout: Optional[int] = None, clear: bool = True
    ) -> None:
        timeout = timeout or self.default_timeout
        if clear:
            self.clear(timeout=timeout)
        element = self.wait_visibility(timeout=timeout)
        Logger.info(f'{self}: text: {keys}', to_file=True)
        try:
            element.send_keys(keys)
            time.sleep(0.5)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            self.driver.dump()
            raise

    def is_displayed(self, timeout: Optional[int] = None) -> bool:
        """Проверяет, виден ли элемент на странице."""
        timeout = timeout or self.default_timeout
        try:
            element = self.wait_visibility(timeout=timeout)
            return element.is_displayed()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            self.driver.dump()
            return False
