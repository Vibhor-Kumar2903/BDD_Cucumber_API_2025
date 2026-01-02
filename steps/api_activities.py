from api.utils.api_helper import API_Client
from api.api_endpoints.activities_swagger import *
from utilities.logger import *
from utilities.json_reader import get_json_data
from behave import *

client = API_Client()


@step('Verify get API')
def getting_activity(context):
    context.response = client.send_request("GET", get_activities, 200)
    response = context.response
    logger.info(response.status_code)
    logger.info(response.json())
    print("API verified")

@step('Verify post API')
def creating_activity(context):
    payload = get_json_data("../api/payloads/activities/", "post_activities.json")
    context.response = client.send_request("POST", post_activities, 200,  payload=payload)
    response = context.response
    logger.info(response.status_code)
    logger.info(response.json())
    context.activity_id = context.response.json()['id']
    print("API verified")


@step('Verify get API by ID')
def Verify_get_API_using_ID(context):
    activities_by_ID = get_activities_by_ID.format(activity_id=context.activity_id)
    context.response = client.send_request('GET', activities_by_ID, 200)
    response = context.response
    logger.info(response.status_code)
    logger.info(response.json())
    print("API verified")


@step('Verify put API by ID')
def put_API_verification(context):
    activities_by_ID = put_activities_by_ID.format(activity_id=context.activity_id)
    payload = get_json_data("../api/payloads/activities/", "put_activities.json")
    context.response = client.send_request('PUT', activities_by_ID, 200, payload=payload)
    response = context.response
    logger.info(response.status_code)
    logger.info(response.json())
    print("API verified")


@step('Verify delete API by ID')
def delete_created_API(context):
    activities_by_ID = delete_activities_by_ID.format(activity_id=context.activity_id)
    context.response = client.send_request('DELETE', activities_by_ID, 200)
    response = context.response
    logger.info(response.status_code)
    print("API verified")




