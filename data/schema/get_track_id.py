GET_TRACK_ID = {
  "type": "object",
  "properties": {
    "tracks": {
      "type": "object",
      "properties": {
        "href": {
          "type": "string"
        },
        "limit": {
          "type": "integer"
        },
        "next": {
          "type": "string"
        },
        "offset": {
          "type": "integer"
        },
        "previous": {
          "type": "null"
        },
        "total": {
          "type": "integer"
        },
        "items": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "album": {
                "type": "object",
                "properties": {
                  "album_type": {
                    "type": "string"
                  },
                  "artists": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
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
                        "href": {
                          "type": "string"
                        },
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string"
                        },
                        "uri": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "external_urls",
                        "href",
                        "id",
                        "name",
                        "type",
                        "uri"
                      ]
                    }
                  },
                  "available_markets": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
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
                  "href": {
                    "type": "string"
                  },
                  "id": {
                    "type": "string"
                  },
                  "images": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "height": {
                          "type": "integer"
                        },
                        "width": {
                          "type": "integer"
                        },
                        "url": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "height",
                        "url",
                        "width"
                      ]
                    }
                  },
                  "is_playable": {
                    "type": "boolean"
                  },
                  "name": {
                    "type": "string"
                  },
                  "release_date": {
                    "type": "string"
                  },
                  "release_date_precision": {
                    "type": "string"
                  },
                  "total_tracks": {
                    "type": "integer"
                  },
                  "type": {
                    "type": "string"
                  },
                  "uri": {
                    "type": "string"
                  }
                },
                "required": [
                  "album_type",
                  "artists",
                  "available_markets",
                  "external_urls",
                  "href",
                  "id",
                  "images",
                  "is_playable",
                  "name",
                  "release_date",
                  "release_date_precision",
                  "total_tracks",
                  "type",
                  "uri"
                ]
              },
              "artists": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
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
                    "href": {
                      "type": "string"
                    },
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    },
                    "uri": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "external_urls",
                    "href",
                    "id",
                    "name",
                    "type",
                    "uri"
                  ]
                }
              },
              "available_markets": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "disc_number": {
                "type": "integer"
              },
              "duration_ms": {
                "type": "integer"
              },
              "explicit": {
                "type": "boolean"
              },
              "external_ids": {
                "type": "object",
                "properties": {
                  "isrc": {
                    "type": "string"
                  }
                },
                "required": [
                  "isrc"
                ]
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
              "href": {
                "type": "string"
              },
              "id": {
                "type": "string"
              },
              "is_local": {
                "type": "boolean"
              },
              "is_playable": {
                "type": "boolean"
              },
              "name": {
                "type": "string"
              },
              "popularity": {
                "type": "integer"
              },
              "preview_url": {
                "type": "null"
              },
              "track_number": {
                "type": "integer"
              },
              "type": {
                "type": "string"
              },
              "uri": {
                "type": "string"
              }
            },
            "required": [
              "album",
              "artists",
              "available_markets",
              "disc_number",
              "duration_ms",
              "explicit",
              "external_ids",
              "external_urls",
              "href",
              "id",
              "is_local",
              "is_playable",
              "name",
              "popularity",
              "preview_url",
              "track_number",
              "type",
              "uri"
            ]
          }
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
    "tracks"
  ]
}