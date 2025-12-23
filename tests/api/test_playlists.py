import allure
import pytest
from allure import step

from data.user_data import PLAYLIST_INFO, TRACK_IDS


@allure.feature("Playlists")
@allure.story("Create and manage playlists")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("layer", "API")
@allure.tag("playlists", "api")
@pytest.mark.skip(
    reason="Flaky due to Spotify's anti-bot protection (reCAPTCHA). Passes locally but fails in headless CI environment",
)
class TestPlaylist:
    @allure.title("Create playlist and add tracks")
    @allure.description("Create new playlist, add tracks, verify tracks are present")
    def test_create_playlist_and_verify_items(self, playlist_client, user_id):
        track_ids = [track_data["id"] for track_data in TRACK_IDS.values()]

        with step("Create playlist"):
            playlist_id = playlist_client.create_playlist(user_id, PLAYLIST_INFO)
            allure.attach(playlist_id, "Playlist ID", allure.attachment_type.TEXT)

        with step("Add tracks to playlist"):
            playlist_client.add_items_to_playlist(playlist_id, track_ids)

        with step("Verify tracks are in playlist"):
            actual_track_ids = playlist_client.get_playlist_items(playlist_id)
            assert actual_track_ids == track_ids
