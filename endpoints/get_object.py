import allure
import requests
from endpoints.base_endpoint import Endpoint

class GetObject(Endpoint):

    @allure.step('Get object by ID')
    def get_by_id(self, object_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{object_id}')
        self.response_json = self.response.json()

    @allure.step('Check that id is correct')
    def check_response_id(self, object_id):
        assert object_id == self.response_json['id']