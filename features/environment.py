from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application



def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # Chrome Web Browser
    #driver_path = ChromeDriverManager().install()

    driver_path = r'C:\Users\faruk\Downloads\internship-project\chromedriver.exe'
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # driver_path = r'C:\Users\faruk\Downloads\internship-project\chromedriver.exe'
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'farisalkassim_J1hq9x'
    # bs_key = 'rxZS5zUJeLaq2Amv4bHA'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "OS X",
    #     "osVersion" : "Sequoia",
    #     'browserName': 'Firefox',
    #     'browserVersion': 'latest',
    #     'sessionName': 'scenario_name',
    #     # 'buildName': 'alpha_0.1.1',
    #     # 'projectName': 'User can see titles and pictures on each product inside the off plan page'
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    # Firefox Web Browser
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    context.driver.maximize_window()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
