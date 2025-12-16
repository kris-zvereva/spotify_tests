import requests
import logging
from typing import Optional, Dict, Any

from config import settings


class SpotifyBaseClient:
    """Base class for all Spotify API clients"""

    BASE_URL = settings.API_BASE_URL

    def __init__(self, auth_headers: Dict[str, str]):
        """
        Args: auth_headers: Dictionary with Authorization headers
        """

        self.headers = auth_headers
        self.logger = logging.getLogger(self.__class__.__name__)

    def _make_request(
            self,
            method: str,
            endpoint: str,
            params: Optional[Dict[str, Any]] = None,
            json: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        """
        Execute HTTP request

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: Endpoint without base URL (e.g.: /tracks/{id})
            params: Query parameters
            json: JSON request body

        Returns: Response object
        """
        url = f"{self.BASE_URL}{endpoint}"

        self.logger.info(f"{method} {url}")
        if params:
            self.logger.debug(f"Params: {params}")
        if json:
            self.logger.debug(f"Body: {json}")

        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            params=params,
            json=json
        )

        self.logger.info(f"Response status: {response.status_code}")
        self.logger.debug(f"Response body: {response.text[:200]}...")

        return response

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Execute GET request"""
        return self._make_request('GET', endpoint, params=params)

    def _post(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Execute POST request"""
        return self._make_request('POST', endpoint, json=json)

    def _put(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Execute PUT request"""
        return self._make_request('PUT', endpoint, json=json)

    def _delete(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Execute DELETE request"""
        return self._make_request('DELETE', endpoint, json=json)