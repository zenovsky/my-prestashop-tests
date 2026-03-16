import logging
from xml.etree import ElementTree as ET

from utils.decorators import log_action

logger = logging.getLogger(__name__)


class CategoriesAPI:
    RESOURCE = "categories"

    def __init__(self, client):
        self.client = client

    @log_action
    def create(self, xml: str) -> int:
        response = self.client.request(method="POST", endpoint=self.RESOURCE, data=xml)
        if response.status_code != 201:
            raise AssertionError(f"Category creation failed: {response.status_code}")
        try:
            root = ET.fromstring(response.text)
            category_id = int(root.find(".//id").text)
        except Exception:
            raise
        return category_id

    @log_action
    def get(self, category_id: int):
        response = self.client.request(method="GET", endpoint=f"{self.RESOURCE}/{category_id}")
        if response.status_code != 200:
            raise AssertionError(f"Failed to get category {category_id}: {response.status_code}")
        root = ET.fromstring(response.text)
        data = {
            "id": root.find(".//id").text,
            "active_status": root.find(".//active").text,
        }
        return data

    @log_action
    def update(self, category_id: int, xml: str) -> int:
        response = self.client.request(method="PUT", endpoint=f"{self.RESOURCE}/{category_id}", data=xml)
        if response.status_code != 200:
            raise AssertionError(
                f"Failed to update category {category_id}: {response.status_code} {response.text[:200]}"
            )

        root = ET.fromstring(response.text)
        data = {
            "id": root.find(".//id").text,
            "active_status": root.find(".//active").text,
        }
        return data

    @log_action
    def delete(self, category_id: int):
        response = self.client.request(method="DELETE", endpoint=f"{self.RESOURCE}/{category_id}")
        if response.status_code != 200:
            raise AssertionError(f"Failed to delete category {category_id}: {response.status_code}")
        return response

    @log_action
    def create_raw(self, xml):
        return self.client.request(method="POST", endpoint=self.RESOURCE, data=xml)

    @log_action
    def update_raw(self, category_id, xml):
        return self.client.request(method="PUT", endpoint=f"{self.RESOURCE}/{category_id}", data=xml)

    @log_action
    def get_raw(self, category_id):
        return self.client.request(method="GET", endpoint=f"{self.RESOURCE}/{category_id}")
