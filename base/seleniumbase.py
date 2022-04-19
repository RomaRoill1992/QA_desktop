
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.common.by import By


def __get_selenium_by(find_by: str) -> dict:
    find_by = find_by.lower()
    locating = {'css': By.CSS_SELECTOR,
                'xpath': By.XPATH,
                'name': By.NAME,
                'id': By.ID,
                'class': By.CLASS_NAME,
                'link': By.LINK_TEXT,
                'tag': By.TAG_NAME}
    return locating[find_by]


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.visibility_of_element_located((__get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.presence_of_element_located((__get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.invisibility_of_element_located((__get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(EC.visibility_of_all_elements_located((__get_selenium_by(find_by), locator)), locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(EC.presence_of_all_elements_located((__get_selenium_by(find_by), locator)), locator_name)

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]

    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

