import logging
from xml.etree import ElementTree as ET

from utils.decorators import log_action

logger = logging.getLogger(__name__)


class ProductsAPI:
    RESOURCE = "products"

    def __init__(self, client):
        self.client = client

    @log_action
    def create(self, xml: str) -> int:
        response = self.client.request(method="POST", endpoint=self.RESOURCE, data=xml)
        if response.status_code != 201:
            raise AssertionError(f"Product creation failed: {response.status_code}")
        try:
            root = ET.fromstring(response.text)
            product_id = int(root.find(".//id").text)
        except Exception:
            raise
        return product_id

    @log_action
    def get(self, product_id: int):
        response = self.client.request(method="GET", endpoint=f"{self.RESOURCE}/{product_id}")
        if response.status_code != 200:
            raise AssertionError(f"Failed to get product {product_id}: {response.status_code}")
        root = ET.fromstring(response.text)
        data = {"id": root.find(".//id").text, "price": root.find(".//price").text}
        return data

    @log_action
    def update(self, product_id: int, xml: str) -> int:
        response = self.client.request(method="PUT", endpoint=f"{self.RESOURCE}/{product_id}", data=xml)
        if response.status_code != 200:
            raise AssertionError(f"Failed to update product {product_id}: {response.status_code} {response.text[:200]}")

        root = ET.fromstring(response.text)
        data = {"id": root.find(".//id").text, "price": root.find(".//price").text}
        return data

    @log_action
    def delete(self, product_id: int):
        response = self.client.request(method="DELETE", endpoint=f"{self.RESOURCE}/{product_id}")
        if response.status_code != 200:
            raise AssertionError(f"Failed to delete product {product_id}: {response.status_code}")
        return response

    @log_action
    def create_raw(self, xml):
        return self.client.request(method="POST", endpoint=self.RESOURCE, data=xml)

    @log_action
    def update_raw(self, product_id, xml):
        return self.client.request(method="PUT", endpoint=f"{self.RESOURCE}/{product_id}", data=xml)

    @log_action
    def get_raw(self, product_id):
        return self.client.request(method="GET", endpoint=f"{self.RESOURCE}/{product_id}")
