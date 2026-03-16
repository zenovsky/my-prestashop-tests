import allure


class AddressScenario:
    def __init__(self, addresses_factory):
        self.addresses_factory = addresses_factory

    @allure.step("Precondition: Existing address")
    def existing_address(self):
        return self.addresses_factory.create()

    @allure.step("Create address")
    def create_address(self):
        return self.addresses_factory.create()

    @allure.step("Get address")
    def get_address(self, address_id):
        return self.addresses_factory.get(address_id)

    @allure.step("Update address")
    def update_address(self, address_data, phone_mobile):
        self.addresses_factory.update(**address_data, new_phone_mobile=phone_mobile)

    @allure.step("Delete address")
    def delete_address(self, address_id):
        return self.addresses_factory.delete(address_id)
