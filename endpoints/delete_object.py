from endpoints.base_endpoint import Endpoint
import allure
import requests

class DeleteObject(Endpoint):
    @allure.step('Delete Object by ID')
    def delete_by_id(self, object_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')


