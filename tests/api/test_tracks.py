import allure
import pytest

from data.user_data import TRACK_1_SEARCH_PARAMS, TRACK_IDS


@allure.feature("Tracks")
@allure.story("Manage favorite tracks")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("layer", "API")
@allure.tag("tracks", "favorites", "api")
@pytest.mark.ci_skip
class TestTracksManagement:
    @allure.title("Add track to favorites")
    @allure.description("Search for track, add to favorites, verify it is saved")
    def test_add_track_to_favs(self, search_client, user_track_client):
        track_id = search_client.get_track_id(TRACK_1_SEARCH_PARAMS)
        assert user_track_client.add_track_to_fav(track_id)
        assert user_track_client.is_track_saved(track_id)

    @allure.title("Delete track from favorites")
    @allure.description("Add track to favorites, then delete and verify removal")
    def test_delete_track_from_favs(self, search_client, user_track_client):
        track_id = search_client.get_track_id(TRACK_1_SEARCH_PARAMS)
        assert user_track_client.add_track_to_fav(track_id)
        assert user_track_client.is_track_saved(track_id)
        assert user_track_client.delete_track_from_fav(track_id)
        assert not user_track_client.is_track_saved(track_id)


@allure.feature("Tracks")
@allure.story("Get track information")
@allure.label("layer", "API")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("tracks", "info", "api")
class TestTrackInfo:
    @allure.title("Get track returns album information")
    @allure.description("Retrieve track by ID and verify album data is present")
    def test_get_track_by_id_returns_album_info(self, track_client):
        track_data = TRACK_IDS["NOGA_EREZ_DUMB"]
        track_info = track_client.get_track_info_by_id(track_data["id"])
        assert "album" in track_info
        assert "name" in track_info["album"]
        assert track_info["album"]["name"] == track_data["album"]

    @pytest.mark.parametrize(
        "track_name, track_data",
        [
            ("NOGA_EREZ_DUMB", TRACK_IDS["NOGA_EREZ_DUMB"]),
            ("SOFIA_ISELLA_DOLL", TRACK_IDS["SOFIA_ISELLA_DOLL"]),
        ],
        ids=["explicit_track", "non_explicit_track"],
    )
    @allure.title("Get track returns explicit flag: {track_name}")
    @allure.description("Retrieve track by ID and verify explicit flag field exists")
    def test_get_track_by_id_returns_explicit_flag(
        self, track_client, track_name, track_data
    ):
        track_info = track_client.get_track_info_by_id(track_data["id"])
        assert "explicit" in track_info
        assert track_info["explicit"] == track_data["explicit"]
