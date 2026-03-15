import allure

class OrderScenario:

    def __init__(self, order_factory):
        self.order_factory = order_factory

    @allure.step("Precondition: Existing order")
    def existing_order(self):
        return self.order_factory.create()
    
    @allure.step("Create order")
    def create_order(self):
        return self.order_factory.create()
    
    @allure.step("Get order")
    def get_order(self, order_id):
        return self.order_factory.get(order_id)

    @allure.step("Update order")
    def update_order(self, order_data, note):
        self.order_factory.update(
            **order_data,
            new_note=note
        )

    @allure.step("Delete order")
    def delete_order(self, order_id):
        return self.order_factory.delete(order_id)    