import logging

from api.models.address_builder import AddressBuilder
from utils.decorators import log_action

logger = logging.getLogger(__name__)


class AddressFactory:
    def __init__(self, addresses_api, customer_factory):
        self.customer_factory = customer_factory
        self.api = addresses_api
        self._ids = []

    @log_action
    def create(self, customer_id=None):
        if not customer_id:
            customer_data = self.customer_factory.create()
            customer_id = customer_data["customer_id"]
        xml = AddressBuilder.create(customer_id=customer_id)
        address_id = self.api.create(xml)
        self._ids.append(address_id)
        return {"address_id": address_id, "customer_id": customer_id}

    @log_action
    def get(self, address_id):
        response = self.api.get(address_id)
        return response

    @log_action
    def update(self, address_id, customer_id, new_phone_mobile):
        xml = AddressBuilder.update(address_id=address_id, customer_id=customer_id, phone_mobile=new_phone_mobile)
        self.api.update(address_id, xml)
        updated_data = self.api.get(address_id)
        assert updated_data["phone_mobile"] == new_phone_mobile

    @log_action
    def delete(self, address_id):
        self.api.delete(address_id)
        try:
            self.api.get(address_id)
            raise AssertionError(f"Address {address_id} still exists after DELETE request!")
        except AssertionError as e:
            if "404" in str(e):
                logger.info(f"Confirmed: Address {address_id} is no longer accessible (404).")
            else:
                raise e

    def cleanup(self):
        for pid in self._ids[:]:
            try:
                self.api.delete(pid)
                logger.info(f"Address cleanup: {pid}")
            except Exception:
                pass
            self._ids.remove(pid)
