import time
from selenium_tests.base_page import BasePage
from selenium_tests.elements.button import Button
from selenium_tests.elements.input import Input
from selenium_tests.elements.web_element import WebElement


class LeadPage(BasePage):

    UNIQUE_ELEMENT_LOC = '//body[@class="yui-skin-sam"]'
    SALES_LOC = '//a[@id="grouptab_0"]'
    LEADS_LOC = '//li[2]//span[2]//ul[1]//li[3]//a[1]'
    #LEADS_LOC = '//a[@id="moduleTab_2_Leads"]'
    PAGE_LEAD_LOC = '//div[@id="content"]'
    CREATE_LEAD_LOC = '//div[normalize-space()="Create Lead"]'
    FIRST_NAME_LOC = '//input[@id ="first_name"]'
    LAST_NAME_LOC = '//input[@id ="last_name"]'
    PHONE_MOBILE_LOC = '//input[@id ="phone_mobile"]'
    SAVE_LOC = '//td[@class="buttons"]//input[@id="SAVE"]'
    LEAD_PAGE_LOC = '//div[@id ="content"]'
    BACK_LOC = "//a[contains(@class, 'suitepicon-action-home')]"

    def __init__(self, driver):
        unique_element = WebElement(
            driver=driver,
            locator=self.UNIQUE_ELEMENT_LOC,
            description="Верхнее меню",
        )
        super().__init__(driver, unique_element)
        self.sales_input = Input(
            driver=self.driver,
            locator=self.SALES_LOC,
            description="Верхнее меню → Marketing",
        )
        self.lead_click = Input(
            driver=self.driver,
            locator=self.LEADS_LOC ,
            description="Верхнее меню → Marketing -> Лиды",
        )
        self.page_lead_wait = Input(
            driver=self.driver,
            locator=self.PAGE_LEAD_LOC ,
            description="Верхнее меню → Marketing -> Лиды -> Страница лида",
        )
        self.create_lead_element = Button(
            driver=self.driver,
            locator=self.CREATE_LEAD_LOC,
            description="Верхнее меню → Marketing -> Лиды -> Создать",
        )
        self.first_name_input = Input(
            driver=self.driver,
            locator=self.FIRST_NAME_LOC,
            description="Верхнее меню → Marketing -> Лиды -> Создать -> Имя",
        )
        self.last_name_input = Input(
            driver=self.driver,
            locator=self.LAST_NAME_LOC,
            description="Верхнее меню → Marketing -> Лиды -> Создать -> Имя -> Фамилия",
        )
        self.phone_mobile_input = Input(
            driver=self.driver,
            locator=self.PHONE_MOBILE_LOC,
            description="Верхнее меню → Marketing -> Лиды -> Создать -> Имя -> Фамилия -> Номер телефона",
        )
        self.save_button = Button(
            driver=self.driver,
            locator=self.SAVE_LOC,
            description="Верхнее меню → Marketing -> Лиды -> Создать -> Имя -> Фамилия -> Номер телефона -> Сохранить",
        )
        self.lead_page_input = Input(
            driver=self.driver,
            locator=self.LEAD_PAGE_LOC,
            description="Верхнее меню → Marketing -> Лиды -> Создать -> Имя -> Фамилия -> Номер телефона -> Сохранить -> Страница успешно созданного лида",
        )
        self.back_button = Button(
            driver=self.driver,
            locator=self.BACK_LOC,
            description="Верхнее меню → Marketing -> Лиды -> Создать -> Имя -> Фамилия -> Номер телефона -> Сохранить -> Страница успешно созданного лида -> Назад",
        )


    def click_save_button(self):
        self.save_button.click()

    def create_lead(self):
        time.sleep(1)
        self.sales_input.click()
        self.lead_click.click()
        time.sleep(1)
        self.page_lead_wait.wait_visibility()
        time.sleep(1)
        self.create_lead_element.click()
        time.sleep(0.5)

    def wait_lead_page(self):
        self.lead_page_input.wait_visibility()
        self.back_button.click()