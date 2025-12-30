import allure
from jsonschema.validators import validate

from api_clients.base_client import SpotifyBaseClient
from data.schema.add_items_to_playlist import (
    ADD_ITEMS_TO_PLAYLIST_REQUEST,
    ADD_ITEMS_TO_PLAYLIST_RESPONSE,
)
from data.schema.create_playlist import (
    CREATE_PLAYLIST_REQUEST,
    CREATE_PLAYLIST_RESPONSE,
)
from data.schema.get_playlist_items import GET_PLAYLIST_ITEMS


class PlaylistClient(SpotifyBaseClient):
    """Client for working with playlists"""

    @allure.step("Create playlist")
    def create_playlist(self, user_id: str, playlist_info: dict) -> str:
        """
        Create playlist
        Args:
        user_id: User ID
        playlist_info: Playlist information (name, description, public)
        Returns: playlist ID
        """
        self.logger.info(f"Creating playlist for user {user_id}")
        validate(instance=playlist_info, schema=CREATE_PLAYLIST_REQUEST)

        response = self._post(f"/users/{user_id}/playlists", json=playlist_info)

        assert response.status_code == 201

        playlist_data = response.json()
        validate(instance=playlist_data, schema=CREATE_PLAYLIST_RESPONSE)
        playlist_id = playlist_data["id"]
        self.logger.info(f"Created playlist ID: {playlist_id}")
        allure.attach(playlist_id, "Playlist ID", allure.attachment_type.TEXT)

        return playlist_id

    @allure.step("Add tracks to playlist")
    def add_items_to_playlist(self, playlist_id: str, track_ids: list) -> dict:
        """
        Add tracks to playlist
        Args:
            playlist_id: Playlist ID
            track_ids: List of track IDs
        Returns: Response data
        """
        self.logger.info(f"Adding {len(track_ids)} tracks to playlist {playlist_id}")
        uris = [f"spotify:track:{track_id}" for track_id in track_ids]
        request_body = {"uris": uris}
        validate(instance=request_body, schema=ADD_ITEMS_TO_PLAYLIST_REQUEST)

        response = self._post(f"/playlists/{playlist_id}/tracks", json=request_body)
        data = response.json()
        assert response.status_code == 201
        validate(instance=data, schema=ADD_ITEMS_TO_PLAYLIST_RESPONSE)

        return data

    @allure.step("Retrieve playlist items")
    def get_playlist_items(self, playlist_id: str) -> list:
        """
        Get track IDs from playlist
        Args: playlist_id: Playlist ID
        Returns: List of track IDs
        """
        self.logger.info(f"Getting items from playlist {playlist_id}")
        response = self._get(f"/playlists/{playlist_id}/tracks")

        assert (
            response.status_code == 200
        ), f"Failed to get playlist items: {response.text}"

        data = response.json()
        validate(instance=data, schema=GET_PLAYLIST_ITEMS)

        track_ids = [item["track"]["id"] for item in data["items"]]
        self.logger.info(f"Found {len(track_ids)} tracks in playlist")

        return track_ids
