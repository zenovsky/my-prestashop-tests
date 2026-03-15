import logging
from api.models.product_builder import ProductBuilder
from utils.decorators import log_action

logger = logging.getLogger(__name__)

class ProductFactory:

    def __init__(self, products_api):
        self.api = products_api
        self._created_ids = []

    @log_action
    def create(self, name="Test product", price=29.90, category_id=4):
        xml = ProductBuilder.create(name=name, price=price, category_id=category_id)
        product_id = self.api.create(xml)
        self._created_ids.append(product_id)
        return {
            "product_id": product_id,
            "name": name,
            "price": price,
            "category_id": category_id
        }

    @log_action
    def get(self, product_id):
        return self.api.get(product_id)

    @log_action
    def update(self, product_id, new_price=None, new_name=None):
        xml = ProductBuilder.update(
            product_id,
            price=new_price,
            name=new_name
        )
        self.api.update(product_id, xml)
        updated_data = self.api.get(product_id)
        if new_price:
            assert float(updated_data['price']) == float(new_price)
        return updated_data    

    @log_action
    def delete(self, product_id):
        self.api.delete(product_id)
        try:
            self.api.get(product_id)
            raise AssertionError(f"Product {product_id} still exists after DELETE request!")
        except AssertionError as e:
            if "404" in str(e):
                logger.info(f"Confirmed: Product {product_id} is no longer accessible (404).")
            else:
                raise e

    @log_action
    def cleanup(self):
        for pid in self._created_ids[:]:
            try:
                self.api.delete(pid)
                logger.info(f"Product cleanup: {pid}")
            except Exception:
                pass
            self._created_ids.remove(pid)