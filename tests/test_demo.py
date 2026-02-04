import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from tests.test_data import payloads
from tests.test_data import expected_results as exp
import allure

@allure.feature("Object Management API")
@allure.severity(allure.severity_level.CRITICAL)
class TestObjectsAPI:
    @allure.story("Create Object")
    @allure.title("Verify creation of a new object")
    @pytest.mark.parametrize('payload', payloads.create_payloads)
    def test_create_object(self,payload):
        new_object_endpoint = CreateObject()
        new_object_endpoint.new_object(payload=payload)
        new_object_endpoint.check_response_is_200()
        new_object_endpoint.check_name(payload['name'])

    @allure.story("Get Object")
    @allure.title("Verify retrieval of a specific object by ID")
    def test_get_object(self, obj_id):
        get_object_endpoint = GetObject()
        get_object_endpoint.get_by_id(obj_id)
        get_object_endpoint.check_response_is_200()
        get_object_endpoint.check_response_id(obj_id)


    @allure.story("Update Object")
    @allure.title("Verify full update (PUT) of an object")
    @pytest.mark.parametrize('payload', payloads.update_payloads)
    def test_update_object(self, obj_id, payload):
        update_object_endpoint = UpdateObject()
        update_object_endpoint.update_by_id(obj_id, payload=payload)
        update_object_endpoint.check_response_is_200()
        update_object_endpoint.check_name(payload['name'])


    @allure.story("Delete Object")
    @allure.title("Verify deletion of an object")
    def test_delete_object(self, obj_id):
        delete_object_endpoint = DeleteObject()
        delete_object_endpoint.delete_by_id(obj_id)
        delete_object_endpoint.check_response_is_200()
        get_object_endpoint = GetObject()
        get_object_endpoint.get_by_id(obj_id)
        get_object_endpoint.check_response_is_404()

    @allure.story("Test flakinness")
    @allure.title("Verify test flakinness")
    @pytest.mark.parametrize('input_value', [1, 2])
    def test_flakinness(self, input_value=1):
        assert 1 == input_value