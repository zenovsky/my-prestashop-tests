import allure


class ProductScenario:

    def __init__(self, products_factory):
        self.products_factory = products_factory

    @allure.step("Precondition: Existing product")
    def existing_product(self, name="Test product", price=29.90):
        return self.products_factory.create(name=name, price=price)
    
    
    @allure.step("Create product")
    def create_product(self, name="Test product", price=29.90):
        return self.products_factory.create(name=name, price=price)
    
    @allure.step("Get product")
    def get_product(self, product_id):
        return self.products_factory.get(product_id)

    @allure.step("Update product")
    def update_product(self, product_data, new_price=None, new_name=None):
        return self.products_factory.update(
            product_id=product_data["product_id"],
            new_price=new_price,
            new_name=new_name
        )
    
    @allure.step("Delete product")
    def delete_product(self, product_id):
        return self.products_factory.delete(product_id)    