import allure

class Endpoint:
    response_json = None
    response = None

    @allure.step('Check that staus is OK')
    def check_response_is_200(self):
        assert self.response.status_code == 200


    @allure.step('Check that staus is 404')
    def check_response_is_404(self):
        assert self.response.status_code == 404