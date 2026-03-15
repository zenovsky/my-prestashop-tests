import logging
from utils.decorators import log_action
from xml.etree import ElementTree as ET

logger = logging.getLogger(__name__)

class OrdersAPI:

    RESOURCE = "orders"

    def __init__(self, client):
        self.client = client

    @log_action
    def create(self, xml: str) -> int:
        response = self.client.request(
            method="POST",
            endpoint=self.RESOURCE,
            data=xml
        )
        if response.status_code != 201:
            raise AssertionError(f"Order creation failed: {response.status_code}")
        try:
            root = ET.fromstring(response.text)
            order_id = int(root.find(".//id").text)
        except Exception as e:
            raise
        return order_id

    @log_action
    def get(self, order_id: int):
        response = self.client.request(
        method="GET",
        endpoint=f"{self.RESOURCE}/{order_id}"
    )
    
        if response.status_code != 200:
            raise AssertionError(f"Failed to get order {order_id}: {response.status_code}")

        root = ET.fromstring(response.text)
    
        data = {
            "id": root.find(".//id").text,
            "note": root.find(".//note").text,
            "id_customer": root.find(".//id_customer").text,
        }
        return data     

    @log_action
    def update(self, order_id: int, xml: str) -> int:
        response = self.client.request(
            method="PUT", 
            endpoint=f"{self.RESOURCE}/{order_id}",
            data=xml
        )
        if response.status_code != 200:
            raise AssertionError(f"Failed to update order {order_id}: {response.status_code} {response.text[:200]}")
        
        root = ET.fromstring(response.text)
        data = {
            "id": root.find(".//id").text,
            "note": root.find(".//note").text,
            "id_customer": root.find(".//id_customer").text,
        }
        return data  

    @log_action
    def delete(self, order_id: int):
        response = self.client.request(
            method="DELETE",
            endpoint=f"{self.RESOURCE}/{order_id}"
        )
        if response.status_code != 200:
            raise AssertionError(f"Failed to delete order {order_id}: {response.status_code}")
        return response