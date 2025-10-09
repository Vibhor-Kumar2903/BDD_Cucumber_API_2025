from selenium.webdriver.support import expected_conditions as EC
from drivers.chrome_driver import launch_chrome, close_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.swag_page import *
from utilities.logger import get_logger
from behave import *

logger = get_logger()

@step('Go to login page')
def invoke_browser(context):
    logger.info(f"Invoking browser and web application.")
    launch_chrome(context)
    context.driver.get("https://www.saucedemo.com/v1/")
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.ID, landing_page)))

@step('Enter the username and password in textbox')
def fill_credential(context):
    logger.info(f"Entering the username and password in textbox.")
    context.driver.find_element(By.ID, user_field).send_keys(username)
    context.driver.find_element(By.ID, pass_field).send_keys(password)

@step('Enter the username {user} and password {pwd} in textbox')
def fill_credential(context, user, pwd):
    logger.info(f"Entering the username and password in textbox by scenario outline.")
    context.driver.find_element(By.ID, user_field).send_keys(user)
    context.driver.find_element(By.ID, pass_field).send_keys(pwd)

@step('Click on login button')
def click_login_button(context):
    logger.info(f"Clicking on login button.")
    context.driver.find_element(By.ID, login_button).click()

@step('Verify the dashboard')
def verify_dashboard_page(context):
    logger.info(f"Verifying the dashboard page.")
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, dashboard)))
    close_driver(context)

