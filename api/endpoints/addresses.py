import logging
from xml.etree import ElementTree as ET

from utils.decorators import log_action

logger = logging.getLogger(__name__)


class AddressesAPI:
    RESOURCE = "addresses"

    def __init__(self, client):
        self.client = client

    @log_action
    def create(self, xml: str) -> int:
        response = self.client.request(method="POST", endpoint=self.RESOURCE, data=xml)
        if response.status_code != 201:
            raise AssertionError(f"Address creation failed: {response.status_code}")
        try:
            root = ET.fromstring(response.text)
            address_id = int(root.find(".//id").text)
        except Exception:
            raise
        return address_id

    @log_action
    def get(self, address_id: int):
        response = self.client.request(method="GET", endpoint=f"{self.RESOURCE}/{address_id}")
        if response.status_code != 200:
            raise AssertionError(f"Failed to get address {address_id}: {response.status_code}")
        root = ET.fromstring(response.text)
        data = {
            "id": root.find(".//id").text,
            "phone_mobile": root.find(".//phone_mobile").text,
            "id_customer": root.find(".//id_customer").text,
        }
        return data

    @log_action
    def update(self, address_id: int, xml: str) -> int:
        response = self.client.request(method="PUT", endpoint=f"{self.RESOURCE}/{address_id}", data=xml)
        if response.status_code != 200:
            raise AssertionError(
                f"Failed to update customer {address_id}: {response.status_code} {response.text[:200]}"
            )

        root = ET.fromstring(response.text)
        data = {
            "id": root.find(".//id").text,
            "phone_mobile": root.find(".//phone_mobile").text,
            "id_customer": root.find(".//id_customer").text,
        }
        return data

    @log_action
    def delete(self, address_id: int):
        response = self.client.request(method="DELETE", endpoint=f"{self.RESOURCE}/{address_id}")
        if response.status_code != 200:
            raise AssertionError(f"Failed to delete address {address_id}: {response.status_code}")
        return response
