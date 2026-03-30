from telnetlib import EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_tests.elements.base_element import BaseElement


class Label(BaseElement):
    """Label Class-wrapper for Selenium WebElement."""

    def is_displayed(self):
        try:
            # Ожидаем, что элемент доступен на странице
            return self.driver.find_element_by_xpath(self.locator).is_displayed()
        except NoSuchElementException:
            # Если элемент не найден, возвращаем False
            return False

    def wait_for_text(self, new_name, timeout=15):
        # Ожидаем до 'timeout' секунд, пока текст элемента не станет равен new_name
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.XPATH, self.locator), new_name)
        )
