CREATE_PLAYLIST_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
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
    "href": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "images": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "url": {
              "type": "string"
            },
            "height": {
              "type": "integer"
            },
            "width": {
              "type": "integer"
            }
          },
          "required": [
            "url",
            "height",
            "width"
          ]
        }
      ]
    },
    "name": {
      "type": "string"
    },
    "owner": {
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
        },
        "display_name": {
          "type": "string"
        }
      },
      "required": [
        "external_urls",
        "href",
        "id",
        "type",
        "uri",
        "display_name"
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
          "type": "string"
        },
        "total": {
          "type": "integer"
        },
        "items": {
          "type": "array",
          "items": [
            {
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
                "track": {
                  "type": "object",
                  "properties": {
                    "album": {
                      "type": "object",
                      "properties": {
                        "album_type": {
                          "type": "string"
                        },
                        "total_tracks": {
                          "type": "integer"
                        },
                        "available_markets": {
                          "type": "array",
                          "items": [
                            {
                              "type": "string"
                            },
                            {
                              "type": "string"
                            },
                            {
                              "type": "string"
                            }
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
                        "images": {
                          "type": "array",
                          "items": [
                            {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "string"
                                },
                                "height": {
                                  "type": "integer"
                                },
                                "width": {
                                  "type": "integer"
                                }
                              },
                              "required": [
                                "url",
                                "height",
                                "width"
                              ]
                            }
                          ]
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
                        "restrictions": {
                          "type": "object",
                          "properties": {
                            "reason": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "reason"
                          ]
                        },
                        "type": {
                          "type": "string"
                        },
                        "uri": {
                          "type": "string"
                        },
                        "artists": {
                          "type": "array",
                          "items": [
                            {
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
                          ]
                        }
                      },
                      "required": [
                        "album_type",
                        "total_tracks",
                        "available_markets",
                        "external_urls",
                        "href",
                        "id",
                        "images",
                        "name",
                        "release_date",
                        "release_date_precision",
                        "restrictions",
                        "type",
                        "uri",
                        "artists"
                      ]
                    },
                    "artists": {
                      "type": "array",
                      "items": [
                        {
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
                      ]
                    },
                    "available_markets": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        }
                      ]
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
                        },
                        "ean": {
                          "type": "string"
                        },
                        "upc": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "isrc",
                        "ean",
                        "upc"
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
                    "is_playable": {
                      "type": "boolean"
                    },
                    "linked_from": {
                      "type": "object"
                    },
                    "restrictions": {
                      "type": "object",
                      "properties": {
                        "reason": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "reason"
                      ]
                    },
                    "name": {
                      "type": "string"
                    },
                    "popularity": {
                      "type": "integer"
                    },
                    "preview_url": {
                      "type": "string"
                    },
                    "track_number": {
                      "type": "integer"
                    },
                    "type": {
                      "type": "string"
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
                    "explicit",
                    "external_ids",
                    "external_urls",
                    "href",
                    "id",
                    "is_playable",
                    "linked_from",
                    "restrictions",
                    "name",
                    "popularity",
                    "preview_url",
                    "track_number",
                    "type",
                    "uri",
                    "is_local"
                  ]
                }
              },
              "required": [
                "added_at",
                "added_by",
                "is_local",
                "track"
              ]
            }
          ]
        }
      },
      "required": [
        "href",
        "limit",
        "next",
        "offset",
        "previous",
        "total",
        "items"
      ]
    },
    "type": {
      "type": "string"
    },
    "uri": {
      "type": "string"
    }
  },
  "required": [
    "collaborative",
    "description",
    "external_urls",
    "href",
    "id",
    "images",
    "name",
    "owner",
    "public",
    "snapshot_id",
    "tracks",
    "type",
    "uri"
  ]
}