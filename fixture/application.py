from selenium import webdriver
from fixture.chrome_options import get_chrome_options
from fixture.session import SessionHelper
from webdriver_manager.chrome import ChromeDriverManager


class Application:

    def __init__(self):
        options = get_chrome_options()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.session = SessionHelper(self)

    def is_valid(self):
        try:
            driver = self.driver
            driver.current_url()
            return True
        except:
            return False

    def open_home_page(self):
        driver = self.driver
        url = 'https://www.yakaboo.ua/'
        driver.get(url)
        driver.delete_all_cookies()

    def destroy(self):
        self.driver.quit()
