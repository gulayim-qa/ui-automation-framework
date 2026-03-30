from abc import ABC


class BasePage(ABC):
    UNIQUE_ELEMENT_LOC = None
    PROGRESSBAR_LOC = None

    def __init__(self, driver, unique_element):
        self.driver = driver
        self.unique_element = unique_element


    def wait_for_open(self) -> None:
         self.unique_element.wait_for_presence()