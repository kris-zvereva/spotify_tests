from jsonschema import validate

from api_clients.base_client import SpotifyBaseClient
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
        response = self._put('/me/tracks', json={'ids': [track_id]})

        # TODO: validate request schema
        # TODO: validate response schema

        return response.status_code == 200

    def is_track_saved(self, track_id: str) -> bool:
        """
        Check if track is in favorites
        Args: track_id: Track ID
        Returns: True if track is saved
        """
        self.logger.info(f"Checking if track {track_id} is saved")
        response = self._get('/me/tracks/contains', params={'ids': track_id})

        assert response.status_code == 200, f"Failed to check track: {response.text}"

        return response.json()[0]

    def delete_track_from_fav(self, track_id: str) -> bool:
        """
        Delete track from favorites
        Args: track_id: Track ID
        Returns: True if successfully deleted
        """
        self.logger.info(f"Deleting track {track_id} from favorites")
        response = self._delete('/me/tracks', json={'ids': [track_id]})

        # TODO: validate request schema
        # TODO: validate response schema

        return response.status_code == 200

    def get_track_info_by_id(self, track_id: str) -> dict:
        """
        Get track information by ID
        Args: track_id: Track ID
        Returns: Dictionary with track information
        """
        self.logger.info(f"Getting track info for {track_id}")
        response = self._get(f'/tracks/{track_id}')

        assert response.status_code == 200, f"Failed to get track: {response.text}"

        data = response.json()
        validate(data, GET_TRACK_INFO)

        return data