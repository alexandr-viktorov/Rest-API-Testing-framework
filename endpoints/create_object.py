import requests
from endpoints.base_endpoint import Endpoint
import allure


class CreateObject(Endpoint):
    @allure.step('Read JSON from response')
    def read_json(self,response):
        print(self.response_json)
        return response.json()

    @allure.step("Create a new object")
    def new_object(self, payload):
        print(payload)
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        print(self.response)
        self.response_json = self.read_json(self.response)

    @allure.step('Check that name is correct')
    def check_name(self, name):
        assert self.response_json['name'] == name