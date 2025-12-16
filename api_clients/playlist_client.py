from jsonschema.validators import validate

from api_clients.base_client import SpotifyBaseClient
from data.schema.get_playlist_items import GET_PLAYLIST_ITEMS


class PlaylistClient(SpotifyBaseClient):
    """Client for working with playlists"""

    def create_playlist(self, user_id: str, playlist_info: dict) -> str:
        """
        Create playlist
        Args:
            user_id: User ID
            playlist_info: Playlist information (name, description, public)
        Returns: playlist ID
        """
        self.logger.info(f"Creating playlist for user {user_id}")

        # TODO: validate request schema

        response = self._post(f'/users/{user_id}/playlists', json=playlist_info)

        assert response.status_code == 201, f"Failed to create playlist: {response.text}"

        playlist_data = response.json()
        #validate(playlist_data, CREATE_PLAYLIST_SCHEMA)

        playlist_id = playlist_data['id']
        self.logger.info(f"Created playlist ID: {playlist_id}")

        return playlist_id

    def add_items_to_playlist(self, playlist_id: str, track_ids: list) -> dict:
        """
        Add tracks to playlist
        Args:
            playlist_id: Playlist ID
            track_ids: List of track IDs
        Returns: Response data
        """
        self.logger.info(f"Adding {len(track_ids)} tracks to playlist {playlist_id}")
        uris = [f'spotify:track:{track_id}' for track_id in track_ids]

        # TODO: validate request schema

        response = self._post(f'/playlists/{playlist_id}/tracks', json={'uris': uris})

        assert response.status_code == 201, f"Failed to add items: {response.text}"

        # TODO: validate response schema

        return response.json()

    def get_playlist_items(self, playlist_id: str) -> list:
        """
        Get track IDs from playlist
        Args: playlist_id: Playlist ID
        Returns: List of track IDs
        """
        self.logger.info(f"Getting items from playlist {playlist_id}")
        response = self._get(f'/playlists/{playlist_id}/tracks')

        assert response.status_code == 200, f"Failed to get playlist items: {response.text}"

        data = response.json()
        validate(data, GET_PLAYLIST_ITEMS)
        # TODO: validate response schema

        track_ids = [item['track']['id'] for item in data['items']]
        self.logger.info(f"Found {len(track_ids)} tracks in playlist")

        return track_ids