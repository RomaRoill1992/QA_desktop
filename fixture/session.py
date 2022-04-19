import time
from selenium.webdriver.common.by import By
from Locators import Home_Locators

H_Loc = Home_Locators()


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logIn(self):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element(By.ID, (H_Loc.customer_menu())).click()
        time.sleep(1)
        driver.find_element(By.ID, "email").click()
        driver.find_element(By.ID, "email").clear()
        __username = "+380958584490"
        driver.find_element(By.ID, "email").send_keys(__username)
        driver.find_element(By.ID, "pass").click()
        driver.find_element(By.ID, "pass").clear()
        __password = "qwerty78"
        driver.find_element(By.ID, "pass").send_keys(__password)
        driver.find_element(By.ID, "button-login-modal").click()
        time.sleep(3)

    def logOut(self):
        driver = self.app.driver
        driver.find_element(By.ID, (H_Loc.customer_menu_show_btn())).click()
        driver.find_element(By.CLASS_NAME, "link_logout").click()
        time.sleep(3)

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logOut()

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements(By.CLASS_NAME, "link_logout"))

