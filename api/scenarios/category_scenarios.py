import allure


class CategoryScenario:
    def __init__(self, categories_factory):
        self.categories_factory = categories_factory

    @allure.step("Precondition: Existing category")
    def existing_category(self, name="Test Category", active_status="1"):
        return self.categories_factory.create(active_status=active_status, name=name)

    @allure.step("Create category")
    def create_category(self, name="Test Category", active_status="1"):
        return self.categories_factory.create(active_status=active_status, name=name)

    @allure.step("Get category")
    def get_category(self, category_id):
        return self.categories_factory.get(category_id)

    @allure.step("Update category")
    def update_category(self, category_data, new_name=None, new_active_status=None):
        self.categories_factory.update(
            category_id=category_data["category_id"], new_name=new_name, new_active_status=new_active_status
        )

    @allure.step("Delete category")
    def delete_category(self, category_id):
        return self.categories_factory.delete(category_id)
