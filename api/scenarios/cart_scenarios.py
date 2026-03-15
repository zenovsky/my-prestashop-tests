import allure

class CartScenario:

    def __init__(self, cart_factory):
        self.cart_factory = cart_factory

    @allure.step("Precondition: Existing cart")
    def existing_cart(self):
        return self.cart_factory.create()
    
    @allure.step("Create cart")
    def create_cart(self):
        return self.cart_factory.create()
    
    @allure.step("Get cart")
    def get_cart(self, cart_id):
        return self.cart_factory.get(cart_id)

    @allure.step("Update cart")
    def update_cart(self, cart_data, quantity):
        self.cart_factory.update(
            **cart_data,
            new_quantity=quantity
        )

    @allure.step("Delete cart")
    def delete_cart(self, cart_id):
        return self.cart_factory.delete(cart_id)    