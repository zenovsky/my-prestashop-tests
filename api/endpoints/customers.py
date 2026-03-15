import logging
from utils.decorators import log_action
from xml.etree import ElementTree as ET

logger = logging.getLogger(__name__)

class CustomersAPI:

    RESOURCE = "customers"

    def __init__(self, client):
        self.client = client

    @log_action
    def create(self, xml: str) -> tuple[int, str]:
        response = self.client.request(
            method="POST",
            endpoint=self.RESOURCE,
            data=xml
        )
        if response.status_code != 201:
            raise AssertionError(f"Customer creation failed: {response.status_code}")
        try:
            root = ET.fromstring(response.text)
            customer_id = int(root.find(".//id").text)
            secure_key = root.find(".//secure_key").text
        except Exception as e:
            raise
        return customer_id, secure_key

    @log_action
    def get(self, customer_id: int):
        response = self.client.request(
        method="GET",
        endpoint=f"{self.RESOURCE}/{customer_id}"
    )
        if response.status_code != 200:
            raise AssertionError(f"Failed to get customer {customer_id}: {response.status_code}")
        root = ET.fromstring(response.text)
        data = {
            "id": root.find(".//id").text,
            "note": root.find(".//note").text,
        }
        return data        

    @log_action
    def update(self, customer_id: int, xml: str) -> int:
        response = self.client.request(
            method="PUT",
            endpoint=f"{self.RESOURCE}/{customer_id}",
            data=xml
        )
        if response.status_code != 200:
            raise AssertionError(f"Failed to update customer {customer_id}: {response.status_code} {response.text[:200]}")

        root = ET.fromstring(response.text)
        data = {
            "id": root.find(".//id").text,
            "note": root.find(".//note").text,
        }
        return data

    @log_action
    def delete(self, customer_id: int):
        response = self.client.request(
            method="DELETE",
            endpoint=f"{self.RESOURCE}/{customer_id}"
        )
        if response.status_code != 200:
            raise AssertionError(f"Failed to delete customer {customer_id}: {response.status_code}")
        return response

    @log_action
    def create_raw(self, xml):
        return self.client.request(
            method="POST",
            endpoint=self.RESOURCE,
            data=xml
        )
    
    @log_action
    def update_raw(self, customer_id, xml):
        return self.client.request(
            method="PUT",
            endpoint=f"{self.RESOURCE}/{customer_id}",
            data=xml
        )

    @log_action
    def get_raw(self, customer_id):
        return self.client.request(
            method="GET",
            endpoint=f"{self.RESOURCE}/{customer_id}"
        )          