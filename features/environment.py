from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.support.wait import WebDriverWait


def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    ### HEADLESS MODE ####
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #service = Service(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    #)

    # FIREFOX
    # service = Service(executable_path='/Users/Sehij/Downloads/geckodriver')
    # context.driver = webdriver.Firefox(service=service)

    context.driver.wait = WebDriverWait(context.driver, 15)

    context.driver.maximize_window()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)

 ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

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
