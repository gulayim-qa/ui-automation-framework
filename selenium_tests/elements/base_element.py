import time
from abc import ABC
from typing import Optional, Union
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium_tests.utils.logger.logger import Logger
from selenium_tests.driver.webdriver import WebDriver
from selenium.webdriver import ActionChains


class BaseElement(ABC):
    """Base Class-wrapper for Selenium WebElement."""

    DEFAULT_TIMEOUT = 20

    def __init__(
            self,
            driver: WebDriver,
            locator: Union[str, tuple],
            description: Optional[str] = None,
            default_timeout: int = DEFAULT_TIMEOUT,
    ) -> None:
        self.driver = driver
        self.default_timeout = default_timeout
        self.description = description if description else str(locator)
        self.actions = ActionChains(driver.driver)

        if isinstance(locator, str):
            if "/" in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator

    def __str__(self) -> str:
        return f'{self.__class__.__name__}[{self.description}]'

    def __repr__(self) -> str:
        return str(self)

    def _wait_for(self, expected_condition, timeout: int):
        Logger.info(f'{self}: wait {expected_condition.__name__}', to_file=True)
        try:
            element = WebDriverWait(self.driver.driver, timeout=timeout).until(
                method=expected_condition(self.locator))
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            self.driver.dump()
            raise

        return element

    def _wait_for_not(self, expected_condition, timeout: int):
        Logger.info(f'{self}: wait for not {expected_condition.__name__}', to_file=True)
        try:
            WebDriverWait(self.driver.driver, timeout=timeout).until_not(
                method=expected_condition(self.locator)
            )
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            self.driver.dump()
            raise

    def wait_clickable(self, timeout: Optional[int] = None) -> WebElement:
        timeout = timeout or self.default_timeout
        return self._wait_for(
            expected_condition=EC.element_to_be_clickable, timeout=timeout
        )

    def wait_visibility(self, timeout: Optional[int] = None) -> WebElement:
        timeout = timeout or self.default_timeout
        return self._wait_for(
            expected_condition=EC.visibility_of_element_located, timeout=timeout
        )

    def wait_for_presence(self, timeout: Optional[int] = None) -> WebElement:
        timeout = timeout or self.default_timeout
        return self._wait_for(
            expected_condition=EC.presence_of_element_located, timeout=timeout
        )

    def wait_for_not_presence(self, timeout: Optional[int] = None) -> None:
        timeout = timeout or self.default_timeout
        self._wait_for_not(
            expected_condition=EC.presence_of_element_located, timeout=timeout
        )

    def click(self, timeout: int = None) -> None:
        timeout = timeout or self.default_timeout
        element = self.wait_clickable(timeout=timeout)
        Logger.info(f'{self}: click', to_file=True)
        try:
            element.click()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            self.driver.dump()
            raise

    def get_text(self, timeout: Optional[int] = None) -> str:
        timeout = timeout or self.default_timeout
        element = self.wait_for_presence(timeout=timeout)
        Logger.info(f'{self}: get element text', to_file=True)
        try:
            text = element.text
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            self.driver.dump()
            raise

        Logger.info(f'{self}: element text: {text}', to_file=True)
        return text

    def get_attribute(self, text, timeout: Optional[int] = None) -> str:
        timeout = timeout or self.default_timeout
        element = self.wait_for_presence(timeout=timeout)
        Logger.info(f'{self}: get attribute', to_file=True)
        try:
            attribute = element.get_attribute(text)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            self.driver.dump()
            raise

        Logger.info(f'{self}: attribute: {attribute}', to_file=True)
        return attribute

    def drag_and_drop(self, other, timeout: Optional[int] = None):
        timeout = timeout or self.default_timeout
        element = self.wait_visibility(timeout=timeout)
        other_element = other.wait_visibility(timeout=timeout)
        self.actions.drag_and_drop(element, other_element).perform()

    def move_to_element(self, timeout: Optional[int] = None):
        timeout = timeout or self.default_timeout
        element = self.wait_visibility(timeout=timeout)
        self.actions.move_to_element(element).perform()
        time.sleep(0.5)