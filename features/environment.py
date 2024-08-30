from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application



def browser_init(context):
    """
    :param context: Behave context
    """
    # Chrome Web Browser
    #driver_path = ChromeDriverManager().install()

    # driver_path = r'C:\Users\faruk\Downloads\internship-project\chromedriver.exe'
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    ### HEADLESS MODE ####
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver_path = r'C:\Users\faruk\Downloads\internship-project\chromedriver.exe'
    service = Service(driver_path)
    context.driver = webdriver.Chrome(
        options=options,
        service=service
    )

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
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
