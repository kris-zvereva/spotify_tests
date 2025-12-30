import allure
from jsonschema.validators import validate

from api_clients.base_client import SpotifyBaseClient
from data.schema.get_track_id import GET_TRACK_ID


class SearchClient(SpotifyBaseClient):
    """Client for search operations"""

    @allure.step("Search for track and return its ID")
    def get_track_id(self, search_params: dict) -> str:
        """
        Search for track and return its ID
        Args: search_params: Search parameters (q, type, limit)
        Returns: ID of the first found track
        """
        self.logger.info(f"Searching tracks with params: {search_params}")
        response = self._get("/search", params=search_params)

        assert response.status_code == 200, f"Search failed: {response.text}"

        search_data = response.json()
        validate(instance=search_data, schema=GET_TRACK_ID)
        tracks = search_data["tracks"]["items"]

        assert len(tracks) > 0, "No tracks found!"

        track_id = tracks[0]["id"]
        self.logger.info(f"Found track ID: {track_id}")
        allure.attach(track_id, "Track ID", allure.attachment_type.TEXT)

        return track_id
