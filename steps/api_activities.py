from api.utils.api_helper import API_Client
from api.api_endpoints.activities_swagger import *
from utilities.logger import *
from utilities.json_reader import get_json_data
from behave import *

client = API_Client()


@step('Verify get API')
def getting_activity(context):
    context.response = client.send_request("GET", get_activities, 200)
    logger.info(context.response.status_code)
    # logger.info(context.response.json())


@step('Verify post API')
def creating_activity(context):
    payload = get_json_data("../api/payloads/activities/", "post_activities.json")
    context.response = client.send_request("POST", post_activities, 200,  payload=payload)
    logger.info(context.response.status_code)
    # logger.info(context.response.json())


# @step(u'Verify get API by ID')
# def step_impl(context):
#     raise StepNotImplementedError(u'When Verify get API by ID')
#
#
# @step(u'Verify post API by ID')
# def step_impl(context):
#     raise StepNotImplementedError(u'When Verify post API by ID')
#
#
# @step(u'Verify delete API by ID')
# def step_impl(context):
#     raise StepNotImplementedError(u'When Verify delete API by ID')



