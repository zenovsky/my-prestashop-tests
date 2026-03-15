import logging

from api.models.order_builder import OrderBuilder
from utils.decorators import log_action

logger = logging.getLogger(__name__)

class OrderFactory:

    def __init__(
        self, 
        orders_api,
        customer_factory,
        address_factory,
        cart_factory
    ):
        self.api = orders_api
        self.customer_factory = customer_factory
        self.address_factory = address_factory
        self.cart_factory = cart_factory
        self._ids = []

    @log_action
    def create(self):
        customer_data = self.customer_factory.create()
        customer_id = customer_data['customer_id']
        secure_key = self.customer_factory.get_secure_key(customer_id)
        address_data = self.address_factory.create(customer_id=customer_id)
        address_id = address_data['address_id']
        cart_data = self.cart_factory.create(
            customer_id=customer_id, 
            address_id=address_id
        )
        cart_id = cart_data['cart_id']

        xml = OrderBuilder.create(
            customer_id=customer_id,
            secure_key=secure_key,
            address_id = address_id,
            cart_id=cart_id 
        )
        order_id = self.api.create(xml)
        self._ids.append(order_id)
        return {
            "order_id": order_id,
            "customer_id": customer_id,
            "address_id": address_id,
            "cart_id": cart_id
        }    
    
    @log_action
    def get(self, order_id):
        response = self.api.get(order_id)
        return response     

    @log_action
    def update(self, order_id, cart_id, customer_id, address_id, new_note):
        xml = OrderBuilder.update(
            order_id=order_id,
            cart_id=cart_id,
            customer_id=customer_id,
            address_id=address_id,
            note=new_note
        )
        self.api.update(order_id, xml)
        updated_data = self.api.get(order_id)
        assert updated_data['note'] == new_note

    @log_action
    def delete(self, order_id):
        self.api.delete(order_id)
        try:
            self.api.get(order_id)
            raise AssertionError(f"Order {order_id} still exists after DELETE request!")
        except AssertionError as e:
            if "404" in str(e):
                logger.info(f"Confirmed: Order {order_id} is no longer accessible (404).")
            else:
                raise e

    @log_action
    def cleanup(self):
        for pid in self._ids[:]:
            try:
                self.api.delete(pid)
                logger.info(f"Order cleanup: {pid}")    
            except Exception:
                pass
            self._ids.remove(pid)