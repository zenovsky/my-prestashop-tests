from xml.etree import ElementTree as ET


class CartsAPI:

    RESOURCE = "carts"

    def __init__(self, client):
        self.client = client

    def create(self, xml: str) -> int:
        response = self.client.request(
            method="POST",
            endpoint=self.RESOURCE,
            data=xml
        )
        if response.status_code != 201:
            raise AssertionError(f"Cart creation failed: {response.status_code}")
        try:
            root = ET.fromstring(response.text)
            cart_id = int(root.find(".//id").text)
        except Exception as e:
            raise
        return cart_id

    def get(self, cart_id: int):
        response = self.client.request(
        method="GET",
        endpoint=f"{self.RESOURCE}/{cart_id}"
    )
        if response.status_code != 200:
            raise AssertionError(f"Failed to get cart {cart_id}: {response.status_code}")
        root = ET.fromstring(response.text)
        data = {
            "id": root.find(".//id").text,
            "id_address_delivery": root.find(".//id_address_delivery").text,
            "id_address_invoice": root.find(".//id_address_invoice").text,
            "id_customer": root.find(".//id_customer").text,
            "id_product": root.find(".//id_product").text,
            "quantity": root.find(".//quantity").text,    
        }
        return data

    def update(self, cart_id: int, xml: str) -> int:
        response = self.client.request(
            method="PUT",
            endpoint=f"{self.RESOURCE}/{cart_id}",
            data=xml
        )
        if response.status_code != 200:
            raise AssertionError(f"Failed to update customer {cart_id}: {response.status_code} {response.text[:200]}")

        root = ET.fromstring(response.text)
        data = {
            "id": root.find(".//id").text,
            "id_address_delivery": root.find(".//id_address_delivery").text,
            "id_address_invoice": root.find(".//id_address_invoice").text,
            "id_customer": root.find(".//id_customer").text,
            "id_product": root.find(".//id_product").text,
            "quantity": root.find(".//quantity").text,
        }
        return data

    def delete(self, cart_id: int):
        response = self.client.request(
            method="DELETE",
            endpoint=f"{self.RESOURCE}/{cart_id}"
        )
        if response.status_code != 200:
            raise AssertionError(f"Failed to delete cart {cart_id}: {response.status_code}")
        return response