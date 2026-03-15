import logging
import allure

from api.models.customer_builder import CustomerBuilder
from utils.decorators import log_action
from utils.data_generator import default_generator

logger = logging.getLogger(__name__)

class CustomerFactory:

    def __init__(self, customers_api):
        self.api = customers_api
        self._ids = []
        self._secure_keys = {}

    @log_action
    def create(
        self, 
        lastname=None,
        firstname=None,
        email=None
    ):
        if lastname is None or firstname is None or email is None:
            user_data = default_generator.generate_user_data()
            lastname = lastname or user_data["lastname"]
            firstname = firstname or user_data["firstname"]
            email = email or user_data["email"]

        allure.attach(
            f"Firstname: {firstname}\nLastname: {lastname}\nEmail: {email}",
            name="Customer Generation Data",
            attachment_type=allure.attachment_type.TEXT
        )    

        xml = CustomerBuilder.create(
            lastname=lastname,
            firstname=firstname,
            email=email
        )
        customer_id, secure_key = self.api.create(xml)
        self._ids.append(customer_id)
        self._secure_keys[customer_id] = secure_key
        return {
            "customer_id": customer_id,
            "lastname": lastname,
            "firstname": firstname,
            "email": email
        }
    
    @log_action
    def get_secure_key(self, customer_id):
        return self._secure_keys.get(customer_id)
    
    @log_action
    def get(self, customer_id):
        response = self.api.get(customer_id)
        return response     

    @log_action
    def update(self, customer_id, lastname, firstname, email, new_note):

        xml = CustomerBuilder.update(
            customer_id=customer_id,
            lastname=lastname,
            firstname=firstname,
            email=email,
            note=new_note

        )
        self.api.update(customer_id, xml)
        updated_data = self.api.get(customer_id)
        assert updated_data['note'] == new_note

    @log_action
    def delete(self, customer_id):
        self.api.delete(customer_id)
        try:
            self.api.get(customer_id)
            raise AssertionError(f"Customer {customer_id} still exists after DELETE request!")
        except AssertionError as e:
            if "404" in str(e):
                logger.info(f"Confirmed: Customer {customer_id} is no longer accessible (404).")
            else:
                raise e

    @log_action                       
    def cleanup(self):
        for pid in self._ids[:]:
            try:
                self.api.delete(pid)
                logger.info(f"Customer cleanup: {pid}")    
            except Exception:
                pass
            self._ids.remove(pid)