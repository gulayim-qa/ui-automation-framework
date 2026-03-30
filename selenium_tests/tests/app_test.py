import time
from datetime import datetime

import pytest
from faker import Faker
from pytest_selenium import driver

from selenium_tests.driver.webdriver import WebDriver
from selenium_tests.project.pages.accounts_page import AccountsPage
from selenium_tests.project.pages.lead_page import LeadPage
from selenium_tests.project.pages.link_lead_to_counterparty_page import LinkLeadToCounterparty
from selenium_tests.project.pages.login_page import LoginPage
from selenium_tests.utils.config_reader import ConfigReader
from selenium_tests.utils.logger.logger import Logger

APP_URL = ""
fake = Faker()


def generate_random_name():
    """Генерация случайного имени."""
    return fake.first_name() + " " + fake.last_name()


def generate_random_phone():
    """Генерация случайного номера телефона."""
    return fake.phone_number()


@pytest.fixture(scope="function")
def app_driver():
    """Фикстура для инициализации и завершения работы WebDriver."""
    driver = WebDriver()
    driver.get(ConfigReader.get_config_value("url"))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_create_lead_and_counterparty(app_driver, driver):
    Logger.info("### Тест: Проверка создания лида, контрагента и их связи", to_file=True)

    # Шаг 1: Авторизация
    app_driver.get(APP_URL)
    login_page = LoginPage(app_driver)
    login_page.wait_for_open()
    login_page.authorization_click(login="test1", password="Trust#@$123")
    time.sleep(1)
    # Шаг 2: Создание лида
    lead_page = LeadPage(app_driver)
    lead_page.wait_for_open()
    lead_page.create_lead()

    lead_first_name = generate_random_name()
    lead_last_name = fake.last_name()
    lead_phone = generate_random_phone()

    lead_page.first_name_input.send_keys(lead_first_name)
    lead_page.last_name_input.send_keys(lead_last_name)
    lead_page.phone_mobile_input.send_keys(lead_phone)
    lead_page.click_save_button()

    lead_page.wait_lead_page()

    assert lead_page.lead_page_input.wait_visibility(), "Лид не был создан!"

    # Шаг 3: Создание контрагента
    accounts_page = AccountsPage(app_driver)
    accounts_page.wait_for_open()
    accounts_page.create_accounts()

    account_name = generate_random_name()
    account_phone = generate_random_phone()

    accounts_page.first_name_accounts.send_keys(account_name)
    accounts_page.phone_mobile_accounts.send_keys(account_phone)
    accounts_page.save_accounts_button.click()

    accounts_page.wait_account_page()
    assert accounts_page.accounts_page_button.wait_visibility(), "Контрагент не был создан!"

    # Шаг 4: Связь лида с контрагентом
    link_page = LinkLeadToCounterparty(app_driver)
    link_page.wait_for_open()
    link_page.test_lead_and_counterparty_link()

    Logger.info(f"Лид: {lead_first_name} {lead_last_name}, Контрагент: {account_name} связаны успешно.", to_file=True)
    Logger.info("### Тест успешно завершен", to_file=True)

    # Проверка, что связь установлена
    assert link_page.page_accounts_button.wait_visibility(), "Связь между лидом и контрагентом не установлена"
    now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
    name_screenshot = 'screenshot' + now_date + '.png'
    driver.save_screenshot('C:\\Users\\Acero\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\Test_Evraz\\selenium_tests\\screen\\' + name_screenshot)