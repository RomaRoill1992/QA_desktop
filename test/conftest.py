import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.logIn()
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


# @pytest.fixture
# def get_chrome_options():
#     options = chrome_options()
#     options.add_argument('chrome')
#     options.add_argument('--start-maximized')
#     return options


# @pytest.fixture
# def get_webdriver(get_chrome_options):
#     options = get_chrome_options
#     driver = webdriver.Chrome(executable_path='C:\\Users\\Roman\\.wdm\\drivers\\chromedriver\\win32\\100.0.4896.60\\chromedriver.exe', options=options)
#     return driver


# @pytest.fixture(scope='function')
# def setup(request, get_webdriver):
#     driver = get_webdriver
#     url = 'https://www.yakaboo.ua/'
#     if request.cls is not None:
#         request.cls.driver = driver
#     driver.get(url)
#     driver.delete_all_cookies()
#     time.sleep(3)
#     yield driver
#     driver.quit()

