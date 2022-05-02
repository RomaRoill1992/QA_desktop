from selenium.webdriver.common.by import By
import time


def test_beta(app):
    app.driver.find_element(By.ID, "yakaboo-top-nav").click()
    time.sleep(2)
    app.driver.find_element(By.CSS_SELECTOR, "//div[@class='left-side']/ul[1]/li[1]/a").click()
    time.sleep(3)
    app.driver.find_element(By.CSS_SELECTOR, ".block6 ul>li:nth-child(3)>a").click()






