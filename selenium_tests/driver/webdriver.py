from typing import Optional
import datetime

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium_tests.utils.config_reader import ConfigReader
from selenium_tests.utils.logger.logger import Logger


class WebDriver:
    """Class-wrapper for Selenium WebDriver."""

    def __init__(self):
        self.DUMPS_DIR = None
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")  # Для запуска в полном окне

        # Устанавливаем драйвер через WebDriverManager
        self.service = ChromeService(ChromeDriverManager().install())
        self._driver = webdriver.Chrome(service=self.service, options=self.options)

    @property
    def driver(self):
        return self._driver

    def get(self, url):
        """Открытие URL."""
        self._driver.get(url)

    def quit(self):
        """Закрытие драйвера."""
        self._driver.quit()


    def maximize_window(self) -> None:
        Logger.info("driver: maximize window", to_file=True)
        try:
            self._driver.maximize_window()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            self.dump()
            raise

    def get_current_url(self):
        Logger.info("driver: get current url", to_file=True)
        return self._driver.current_url


    def save_screenshot(self, screenshot_path: Optional[str] = None) -> None:
        screenshot_path = (
            screenshot_path
            if screenshot_path
            else self.DUMPS_DIR + '/' + f"{datetime.datetime.now().strftime('%d_%m_%Y-%I_%M_%S')}.png"
        )
        Logger.info(f"{self}: take screenshot")
        self._driver.save_screenshot(screenshot_path)

    def dump(self) -> None:
        Logger.info(f"{self}: make dump in '{self.DUMPS_DIR}'")
        # Сохранить DOM
        with open(f"{self.DUMPS_DIR}/{self._driver.title}.html", mode="w", encoding="utf-8") as file:
            file.write(self._driver.page_source)
        # Сохранить скриншот
        self.save_screenshot(f"{self.DUMPS_DIR}/screenshot.png")

    def find_element_by_xpath(self, locator):
        """Поиск элемента по XPath."""
        try:
            # Используем современный способ поиска элементов
            element = self._driver.find_element(By.XPATH, locator)
            return element
        except NoSuchElementException:
            # Логируем и возвращаем None, если элемент не найден
            print(f"Элемент с локатором {locator} не найден.")
            return None

    def execute_script(self, script: str, *args):
        """Выполнение JavaScript через WebDriver."""
        try:
            return self._driver.execute_script(script, *args)
        except WebDriverException as err:
            Logger.error(f"{self}: Ошибка при выполнении скрипта: {err}")
            self.dump()
            raise

    @pytest.fixture(scope="session")
    def driver(self):
        """Фикстура для управления драйвером."""
        driver = WebDriver()
        yield driver
        driver.quit()

    def test_open_page(driver):
        """Тест открытия страницы."""
        url = "https://the-internet.herokuapp.com"
        driver.get(url)
        assert "Example" in driver.driver.title