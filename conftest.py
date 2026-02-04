import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject



@pytest.fixture()
def obj_id():
    payload = {
        "name": "Example Device",
        "data": {
            "year": 2024,
            "price": 999.99,
            "CPU model": "Intel Core i7-13700K",
            "Hard disk size": "1 TB"
        }
    }
    create_object = CreateObject()
    create_object.new_object(payload)
    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_by_id(create_object.response_json['id'])

def pytest_addoption(parser):
    parser.addoption("--value", action="store", default=1)