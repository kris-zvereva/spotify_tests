CREATE_PLAYLIST_REQUEST = {
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "public": {
      "type": "boolean"
    }
  },
  "required": [
    "description",
    "name",
    "public"
  ]
}

CREATE_PLAYLIST_RESPONSE = {
  "type": "object",
  "properties": {
    "collaborative": {
      "type": "boolean"
    },
    "description": {
      "type": "string"
    },
    "external_urls": {
      "type": "object",
      "properties": {
        "spotify": {
          "type": "string"
        }
      },
      "required": [
        "spotify"
      ]
    },
    "followers": {
      "type": "object",
      "properties": {
        "href": {
          "type": "null"
        },
        "total": {
          "type": "integer"
        }
      },
      "required": [
        "href",
        "total"
      ]
    },
    "href": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "images": {
      "type": "array"
    },
    "primary_color": {
      "type": "null"
    },
    "name": {
      "type": "string"
    },
    "type": {
      "type": "string"
    },
    "uri": {
      "type": "string"
    },
    "owner": {
      "type": "object",
      "properties": {
        "href": {
          "type": "string"
        },
        "id": {
          "type": "string"
        },
        "type": {
          "type": "string"
        },
        "uri": {
          "type": "string"
        },
        "display_name": {
          "type": "null"
        },
        "external_urls": {
          "type": "object",
          "properties": {
            "spotify": {
              "type": "string"
            }
          },
          "required": [
            "spotify"
          ]
        }
      },
      "required": [
        "display_name",
        "external_urls",
        "href",
        "id",
        "type",
        "uri"
      ]
    },
    "public": {
      "type": "boolean"
    },
    "snapshot_id": {
      "type": "string"
    },
    "tracks": {
      "type": "object",
      "properties": {
        "limit": {
          "type": "integer"
        },
        "next": {
          "type": "null"
        },
        "offset": {
          "type": "integer"
        },
        "previous": {
          "type": "null"
        },
        "href": {
          "type": "string"
        },
        "total": {
          "type": "integer"
        },
        "items": {
          "type": "array"
        }
      },
      "required": [
        "href",
        "items",
        "limit",
        "next",
        "offset",
        "previous",
        "total"
      ]
    }
  },
  "required": [
    "collaborative",
    "description",
    "external_urls",
    "followers",
    "href",
    "id",
    "images",
    "name",
    "owner",
    "primary_color",
    "public",
    "snapshot_id",
    "tracks",
    "type",
    "uri"
  ]
}