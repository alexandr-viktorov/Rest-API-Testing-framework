from endpoints.base_endpoint import Endpoint
import allure
import requests

class UpdateObject(Endpoint):

    @allure.step('Update object by id')
    def update_by_id(self, object_id, payload):
        self.response = requests.put(f'https://api.restful-api.dev/objects/{object_id}', json=payload)
        self.response_json = self.response.json()

    @allure.step('Check that name is correct')
    def check_name(self, name):
        assert self.response_json['name'] == name