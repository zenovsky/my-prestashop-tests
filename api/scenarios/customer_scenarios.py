import allure

class CustomerScenario:

    def __init__(self, customers_factory):
        self.customers_factory = customers_factory

    @allure.step("Precondition: Existing customer")
    def existing_customer(self):
        customer_data = self.customers_factory.create()
        return customer_data    

    @allure.step("Create customer")
    def create_customer(self):
        return self.customers_factory.create()
    
    @allure.step("Get customer")
    def get_customer(self, customer_id):
        return self.customers_factory.get(customer_id)

    @allure.step("Update customer")
    def update_customer(self, customer_data, lastname=None, firstname=None, email=None, note=None):
        self.customers_factory.update(
            customer_id=customer_data["customer_id"],
            lastname=lastname or customer_data["lastname"],
            firstname=firstname or customer_data["firstname"],
            email=email or customer_data["email"],
            new_note=note
        )

    @allure.step("Delete customer")
    def delete_customer(self, customer_id):
        return self.customers_factory.delete(customer_id)    