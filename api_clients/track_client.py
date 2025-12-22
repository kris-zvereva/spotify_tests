from jsonschema import validate

from api_clients.base_client import SpotifyBaseClient
from data.schema.add_track import ADD_TRACK
from data.schema.delete_track import DELETE_TRACK
from data.schema.get_track_info import GET_TRACK_INFO


class TrackClient(SpotifyBaseClient):
    """Client for working with tracks"""

    def add_track_to_fav(self, track_id: str) -> bool:
        """
        Add track to favorites
        Args: track_id: Track ID
        Returns:  True if added
        """
        self.logger.info(f"Adding track {track_id} to favorites")
        request_body = {"ids": [track_id]}
        validate(instance=request_body, schema=ADD_TRACK)

        response = self._put("/me/tracks", json=request_body)

        return response.status_code == 200

    def is_track_saved(self, track_id: str) -> bool:
        """
        Check if track is in favorites
        Args: track_id: Track ID
        Returns: True if track is saved
        """
        self.logger.info(f"Checking if track {track_id} is saved")
        response = self._get("/me/tracks/contains", params={"ids": track_id})

        assert response.status_code == 200
        return response.json()[0]

    def delete_track_from_fav(self, track_id: str) -> bool:
        """
        Delete track from favorites
        Args: track_id: Track ID
        Returns: True if successfully deleted
        """
        self.logger.info(f"Deleting track {track_id} from favorites")
        request_body = {"ids": [track_id]}
        validate(instance=request_body, schema=DELETE_TRACK)

        response = self._delete("/me/tracks", json={"ids": [track_id]})

        return response.status_code == 200

    def get_track_info_by_id(self, track_id: str) -> dict:
        """
        Get track information by ID
        Args: track_id: Track ID
        Returns: Dictionary with track information
        """
        self.logger.info(f"Getting track info for {track_id}")
        response = self._get(f"/tracks/{track_id}")

        assert response.status_code == 200

        data = response.json()
        validate(instance=data, schema=GET_TRACK_INFO)

        return data
