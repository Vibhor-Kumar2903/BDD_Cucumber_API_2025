from utilities.logger import *
from api.api_endpoints.activities_swagger import activities_base_url as base_url
import requests


class API_Client:
    def __init__(self):
        self.header = {
            'Content-Type': 'application/json'
        }

    def send_request(self, request_type, endpoint, expected_code, payload=None):
        response = None
        logger.info(f"\nSending {request_type} request .....")
        url = f"{base_url}{endpoint}"
        print(f"URL : {url}")

        if request_type == "GET":
            response = requests.get(url=url, headers=self.header, json=payload)

        if request_type == "POST":
            response = requests.post(url=url, headers=self.header, json=payload)

        if request_type == "PUT":
            response = requests.put(url=url, headers=self.header, json=payload)

        if request_type == "DELETE":
            response = requests.delete(url=url, headers=self.header, json=payload)

        print(f"Response : {response}")
        assert response.status_code == expected_code

        return response


