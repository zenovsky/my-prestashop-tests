import logging
from api.models.cart_builder import CartBuilder
from utils.decorators import log_action

logger = logging.getLogger(__name__)

class CartFactory:

    def __init__(
        self, 
        carts_api,
        customer_factory,
        address_factory,
        product_factory
    ):
        self.api = carts_api
        self.customer_factory = customer_factory
        self.address_factory = address_factory
        self.product_factory = product_factory
        self._ids = []

    @log_action
    def create(self, customer_id=None, address_id=None):
        product_data = self.product_factory.create()
        product_id = product_data['product_id']
        if not customer_id:
            customer_data = self.customer_factory.create()
            customer_id = customer_data['customer_id']
        if not address_id:
            address_data = self.address_factory.create(customer_id=customer_id)
            address_id = address_data['address_id']
        xml = CartBuilder.create(
            address_id = address_id,
            customer_id=customer_id,
            product_id=product_id
        )
        cart_id = self.api.create(xml)
        self._ids.append(cart_id)
        return {
            "cart_id": cart_id,
            "address_id": address_id,
            "customer_id": customer_id,
            "product_id": product_id
        }
    
    @log_action
    def get(self, cart_id):
        response = self.api.get(cart_id)
        return response     

    @log_action
    def update(
            self, 
            cart_id, 
            address_id, 
            customer_id, 
            product_id, 
            new_quantity
        ):
        xml = CartBuilder.update(
            cart_id=cart_id,
            address_id=address_id,
            customer_id=customer_id,
            product_id=product_id,
            quantity=new_quantity
        )
        self.api.update(cart_id, xml)
        updated_data = self.api.get(cart_id)
        assert updated_data['quantity'] == new_quantity

    @log_action
    def delete(self, cart_id):
        self.api.delete(cart_id)
        try:
            self.api.get(cart_id)
            raise AssertionError(f"Cart {cart_id} still exists after DELETE request!")
        except AssertionError as e:
            if "404" in str(e):
                logger.info(f"Confirmed: Cart {cart_id} is no longer accessible (404).")
            else:
                raise e

    @log_action           
    def cleanup(self):
        for pid in self._ids[:]:
            try:
                self.api.delete(pid)
                logger.info(f"Address cleanup: {pid}")   
            except Exception:
                pass
            self._ids.remove(pid)