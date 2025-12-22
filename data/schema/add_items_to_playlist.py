ADD_ITEMS_TO_PLAYLIST_REQUEST = {
    "type": "object",
    "properties": {"uris": {"type": "array", "items": {"type": "string"}}},
    "required": ["uris"],
}

ADD_ITEMS_TO_PLAYLIST_RESPONSE = {
    "type": "object",
    "properties": {"snapshot_id": {"type": "string"}},
    "required": ["snapshot_id"],
}
