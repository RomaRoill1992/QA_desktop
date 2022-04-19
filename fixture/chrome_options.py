from selenium.webdriver.chrome.options import Options as chrome_options

""" List of Chromium Command Line Switches 
    https://peter.sh/experiments/chromium-command-line-switches/
"""


def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options
