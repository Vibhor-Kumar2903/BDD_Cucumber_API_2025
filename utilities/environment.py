from drivers.chrome_driver import *
from utilities.logger import *

# logger = get_logger()

def before_all(context):
    launch_chrome(context)


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        logger.info(f"Scenario failed: {scenario.name}, keep browser open for debugging.")
    else:
        logger.info(f"Scenario failed: {scenario.name}")

    context.driver.delete_all_cookies()
    context.driver.get("about:blank")


def after_all(context):
    logger.info("Closing browser after all scenario.")
    context.driver.quit()



