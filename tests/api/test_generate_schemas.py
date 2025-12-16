
import pytest
import requests
from pathlib import Path
from utils.schema_generator import generate_schema_from_response

ENDPOINTS = {
    "playlist_tracks_response": {
        "url": "https://api.spotify.com/v1/playlists/5l3IZuiiyVVzRGG97Ir2Ue/tracks",  # публичный плейлист
        "params": {}
    }
}

@pytest.mark.skip_in_ci  # чтобы случайно не запустился
def test_generate_schemas(client_credentials_token):
    """Одноразовый тест для генерации схем"""
    SCHEMA_DIR = Path(__file__).parent.parent.parent / "data" / "schema"
    SCHEMA_DIR.mkdir(parents=True, exist_ok=True)

    for schema_name, endpoint_info in ENDPOINTS.items():
        response = requests.get(
            endpoint_info["url"],
            headers=client_credentials_token,
            params=endpoint_info["params"]
        )
        assert response.status_code == 200

        output_path = SCHEMA_DIR / f"{schema_name}.json"
        generate_schema_from_response(response, str(output_path))
        print(f"✅ {schema_name}.json")