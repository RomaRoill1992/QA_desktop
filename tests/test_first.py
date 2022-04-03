import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pom.homepage_nav import HomepageNavigation


@pytest.mark.usefixtures('setup')
class Test_homepage:

    def test_nav(self):
        homepage_nav = HomepageNavigation(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validating Nav Link Text'
        # homepage_nav.get_nav_link_by_name('Доставка').click()
        for indx in range(6):
            homepage_nav.get_nav_links()[indx].click()
            time.sleep(1)

    # def test_app_dynamics_job(self):
    #     driver = self.driver
    #     time.sleep(3)
    #     driver.find_element(By.XPATH, "/html/body/div[10]//div/div/div[1]/button[1]/text()").click()
    #     driver.find_element(By.XPATH, "//div[@id='customer_menu']/ul/li/a/span").click()
    #     driver.find_element(By.ID, "email").click()
    #     driver.find_element(By.ID, "email").clear()
    #     driver.find_element(By.ID, "email").send_keys("+380958584490")
    #     driver.find_element(By.ID, "pass").click()
    #     driver.find_element(By.ID, "pass").clear()
    #     driver.find_element(By.ID, "pass").send_keys("qwerty78")
    #     driver.find_element(By.ID, "button-login-modal").click()


