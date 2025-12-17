GET_PLAYLIST_ITEMS = {
  "type": "object",
  "properties": {
    "href": {
      "type": "string"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "added_at": {
            "type": "string"
          },
          "added_by": {
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
              "type",
              "uri"
            ]
          },
          "is_local": {
            "type": "boolean"
          },
          "primary_color": {
            "type": "null"
          },
          "track": {
            "type": "object",
            "properties": {
              "preview_url": {
                "type": "null"
              },
              "available_markets": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "explicit": {
                "type": "boolean"
              },
              "type": {
                "type": "string"
              },
              "episode": {
                "type": "boolean"
              },
              "track": {
                "type": "boolean"
              },
              "album": {
                "type": "object",
                "properties": {
                  "available_markets": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "type": {
                    "type": "string"
                  },
                  "album_type": {
                    "type": "string"
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
                        "url": {
                          "type": "string"
                        },
                        "width": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "height",
                        "url",
                        "width"
                      ]
                    }
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
                  "uri": {
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
                  "total_tracks": {
                    "type": "integer"
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
              "disc_number": {
                "type": "integer"
              },
              "track_number": {
                "type": "integer"
              },
              "duration_ms": {
                "type": "integer"
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
              "name": {
                "type": "string"
              },
              "popularity": {
                "type": "integer"
              },
              "uri": {
                "type": "string"
              },
              "is_local": {
                "type": "boolean"
              }
            },
            "required": [
              "album",
              "artists",
              "available_markets",
              "disc_number",
              "duration_ms",
              "episode",
              "explicit",
              "external_ids",
              "external_urls",
              "href",
              "id",
              "is_local",
              "name",
              "popularity",
              "preview_url",
              "track",
              "track_number",
              "type",
              "uri"
            ]
          },
          "video_thumbnail": {
            "type": "object",
            "properties": {
              "url": {
                "type": "null"
              }
            },
            "required": [
              "url"
            ]
          }
        },
        "required": [
          "added_at",
          "added_by",
          "is_local",
          "primary_color",
          "track",
          "video_thumbnail"
        ]
      }
    },
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
    "total": {
      "type": "integer"
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