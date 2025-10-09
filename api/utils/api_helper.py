from utilities.logger import get_logger
import requests

logger = get_logger()

class API_Client:
    base_url = "https://jsonplaceholder.typicode.com/"

    def __init__(self):
        self.header = {
            'Content-Type': 'application/json'
        }

    def send_request(self, request_type, endpoint, expected_code, payload=None):
        logger.info(f"\nSending {request_type} request .....")
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url=url, headers=self.header, json=payload)
        assert response.status_code == expected_code
        return response


    # def post_request(self, endpoint, response_code, payload=None):
    #     logger.info(f"Sending POST request.....")
    #     url = f"{self.base_url}/{endpoint}"
    #     response = requests.post(url=url, headers=self.header, json=payload)
    #     assert response.status_code == response_code
    #     return response
    #
    # def get_request(self, endpoint, response_code):
    #     logger.info(f"Sending GET request.....")
    #     url = f"{self.base_url}/{endpoint}"
    #     response = requests.get(url=url,  headers=self.header)
    #     assert response.status_code == response_code
    #
    # def put_request(self, endpoint, response_code, payload=None):
    #     logger.info(f"Sending PUT request.....")
    #     url = f"{self.base_url}/{endpoint}"
    #     response = requests.put(url=url,  headers=self.header, json=payload)
    #     assert response.status_code == response_code
    #
    # def patch_request(self, endpoint, response_code, payload=None):
    #     logger.info(f"Sending PATCH request.....")
    #     url = f"{self.base_url}/{endpoint}"
    #     response = requests.patch(url=url, headers=self.header, json=payload)
    #     assert response.status_code == response_code
    #
    # def delete_request(self, endpoint):
    #     logger.info(f"Sending DELETE request.....")
    #     url = f"{self.base_url}/{endpoint}"
    #     response = requests.delete(url=url, headers=self.header)
    #     assert response.status_code == 204