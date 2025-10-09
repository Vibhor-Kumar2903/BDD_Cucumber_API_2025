from behave.runner import Context
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def launch_chrome(context: Context) -> webdriver.Chrome:
    chrome_option = Options()
    chrome_option.add_experimental_option("detach", True)
    chrome_option.add_argument("--disable-notification")
    chrome_option.add_argument("--headless")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    return context.driver


def close_driver(context):
    context.driver.close()
