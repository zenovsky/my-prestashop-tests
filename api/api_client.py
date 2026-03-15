import base64
import logging
import time
from xml.etree import ElementTree as ET

import requests

from config import API_KEY, API_URL

logger = logging.getLogger("HTTP")


class APIClient:
    def __init__(self, base_url: str = None, api_key: str = None):
        self.base_url = (base_url or API_URL).rstrip("/")
        self.api_key = api_key or API_KEY
        auth_str = base64.b64encode(f"{self.api_key}:".encode()).decode()
        self.session = requests.Session()
        self.session.headers.update(
            {"Authorization": f"Basic {auth_str}", "Content-Type": "application/xml", "Accept": "application/xml"}
        )

    def request(self, method, endpoint, **kwargs):
        endpoint = endpoint.lstrip("/")
        url = f"{self.base_url}/{endpoint}"
        if "data" in kwargs:
            logger.debug(f"Request playload:\n{kwargs['data']}")
        start = time.time()
        response = self.session.request(method=method, url=url, **kwargs)
        duration = round(time.time() - start, 2)
        logger.info(f"{method.upper():6} /{endpoint:<20} {response.status_code} ({duration}s)")
        logger.debug(f"Response body:\n{response.text[:500]}")

        return response

    def get(self, resource, resource_id=None, params=None):
        endpoint = f"{resource}/{resource_id}" if resource_id else resource
        return self._request("GET", endpoint, params=params)

    def post(self, resource, data):
        return self._request("POST", resource, data=data)

    def put(self, resource, resource_id, data):
        endpoint = f"{resource}/{resource_id}"
        return self._request("PUT", endpoint, data=data)

    def delete(self, resource, resource_id):
        endpoint = f"{resource}/{resource_id}"
        return self._request("DELETE", endpoint)

    @staticmethod
    def parse_xml(xml):
        return ET.fromstring(xml)

    @staticmethod
    def get_id_from_response(xml):
        root = ET.fromstring(xml)
        return int(root.find(".//id").text)
