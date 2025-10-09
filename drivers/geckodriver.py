from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


def launch_firefox(context):
    gecko_option = Options()
    gecko_option.add_argument("detach")
    context.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=gecko_option)
    context.driver.maximize_window()
    return context.driver
