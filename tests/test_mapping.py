# import json
#
#
# def test_mapping(app):
#     """Test of mapping."""
#     search = app.extensions['invenio-search']
#     with open(search.mappings['records-record-v1.0.0']) as f:
#         data = json.load(f)
#     assert data == {
#   "mappings": {
#     "date_detection": False,
#     "numeric_detection": False,
#     "properties": {
#       "_access": {
#         "type": "object",
#         "properties": {
#           "metadata_restricted": {
#             "type": "boolean"
#           },
#           "files_restricted": {
#             "type": "boolean"
#           }
#         }
#       },
#       "_bucket": {
#         "enabled": False
#       },
#       "_conceptrecid": {
#         "type": "keyword"
#       },
#       "_created_by": {
#         "type": "integer"
#       },
#       "_default_preview": {
#         "enabled": False
#       },
#       "_files": {
#         "type": "object",
#         "properties": {
#           "bucket": {
#             "type": "keyword"
#           },
#           "key": {
#             "type": "keyword",
#             "copy_to": "filename"
#           },
#           "version_id": {
#             "type": "keyword"
#           },
#           "size": {
#             "type": "long"
#           },
#           "checksum": {
#             "type": "keyword"
#           },
#           "previewer": {
#             "type": "keyword"
#           },
#           "type": {
#             "type": "keyword",
#             "copy_to": "filetype"
#           }
#         }
#       },
#       "_internal_notes": {
#         "type": "object",
#         "properties": {
#           "user": {
#             "type": "keyword"
#           },
#           "note": {
#             "type": "text"
#           },
#           "timestamp": {
#             "type": "date"
#           }
#         }
#       },
#       "_recid": {
#         "type": "keyword"
#       },
#       "_oai": {
#         "type": "object",
#         "properties": {
#           "id": {
#             "type": "keyword"
#           },
#           "sets": {
#             "type": "keyword"
#           },
#           "updated": {
#             "type": "date"
#           }
#         }
#       },
#       "_owners": {
#         "type": "integer"
#       },
#       "_embargo_date": {
#         "type": "date"
#       },
#       "_contact": {
#         "type": "keyword"
#       },
#       "_communities": {
#         "type": "object",
#         "properties": {
#           "accepted": {
#             "type": "object",
#             "properties": {
#               "id": {
#                 "type": "keyword"
#               },
#               "comid": {
#                 "type": "keyword"
#               },
#               "title": {
#                 "type": "text"
#               },
#               "request_id": {
#                 "type": "keyword"
#               },
#               "created_by": {
#                 "type": "integer"
#               }
#             }
#           },
#           "pending": {
#             "type": "object",
#             "properties": {
#               "id": {
#                 "type": "keyword"
#               },
#               "comid": {
#                 "type": "keyword"
#               },
#               "title": {
#                 "type": "text"
#               },
#               "request_id": {
#                 "type": "keyword"
#               },
#               "created_by": {
#                 "type": "integer"
#               }
#             }
#           },
#           "rejected": {
#             "type": "object",
#             "properties": {
#               "id": {
#                 "type": "keyword"
#               },
#               "comid": {
#                 "type": "keyword"
#               },
#               "title": {
#                 "type": "text"
#               },
#               "request_id": {
#                 "type": "keyword"
#               },
#               "created_by": {
#                 "type": "integer"
#               }
#             }
#           }
#         }
#       },
#       "access_right": {
#         "type": "keyword"
#       },
#       "resource_type": {
#         "type": "object",
#         "properties": {
#           "type": {
#             "type": "keyword"
#           },
#           "subtype": {
#             "type": "keyword"
#           }
#         }
#       },
#       "identifiers": {
#         "type": "object"
#       },
#       "creators": {
#         "type": "object",
#         "properties": {
#           "name": {
#             "type": "text"
#           },
#           "type": {
#             "type": "keyword"
#           },
#           "given_name": {
#             "type": "text"
#           },
#           "family_name": {
#             "type": "text"
#           },
#           "identifiers": {
#             "type": "object"
#           },
#           "affiliations": {
#             "type": "object",
#             "properties": {
#               "name": {
#                 "type": "text"
#               },
#               "identifiers": {
#                 "type": "object"
#               }
#             }
#           }
#         }
#       },
#       "titles": {'type': 'object', 'properties':
#                     {
#                         'cs': {'type': 'text',
#                                'fields': {
#                                    "keywords": {
#                                        "type": "keyword"
#                                    }
#                                }},
#                         'en': {'type': 'text',
#                                'fields': {
#                                    "keywords": {
#                                        "type": "keyword"
#                                    }
#                                }
#                                }
#                     }
#                           },
#       "subjects": {'type': 'object', 'properties':
#                     {
#                         'cs': {'type': 'text',
#                                'fields': {
#                                    "keywords": {
#                                        "type": "keyword"
#                                    }
#                                }},
#                         'en': {'type': 'text',
#                                'fields': {
#                                    "keywords": {
#                                        "type": "keyword"
#                                    }
#                                }
#                                }
#                     }
#                           },
#       "contributors": {
#         "type": "object",
#         "properties": {
#           "name": {
#             "type": "text"
#           },
#           "type": {
#             "type": "keyword"
#           },
#           "given_name": {
#             "type": "text"
#           },
#           "family_name": {
#             "type": "text"
#           },
#           "identifiers": {
#             "type": "object"
#           },
#           "affiliations": {
#             "type": "object",
#             "properties": {
#               "name": {
#                 "type": "text"
#               },
#               "identifiers": {
#                 "type": "object"
#               }
#             }
#           },
#           "role": {
#             "type": "keyword"
#           }
#         }
#       },
#       "dates": {
#         "type": "object",
#         "properties": {
#           "start": {
#             "type": "date"
#           },
#           "end": {
#             "type": "date"
#           },
#           "type": {
#             "type": "keyword"
#           },
#           "description": {'type': 'text'}
#         }
#       },
#       "language": {
#         "type": "keyword"
#       },
#       "related_identifiers": {
#         "type": "object",
#         "properties": {
#           "identifier": {
#             "type": "keyword",
#             "copy_to": "related.identifier"
#           },
#           "scheme": {
#             "type": "keyword"
#           },
#           "relation_type": {
#             "type": "keyword"
#           },
#           "resource_type": {
#             "properties": {
#               "subtype": {
#                 "type": "keyword"
#               },
#               "type": {
#                 "type": "keyword"
#               }
#             }
#           }
#         }
#       },
#       "version": {
#         "type": "keyword"
#       },
#       "licenses": {
#         "type": "object",
#         "properties": {
#           "license": {'type': 'object', 'properties':
#                     {
#                         'cs': {'type': 'text',
#                                'fields': {
#                                    "keywords": {
#                                        "type": "keyword"
#                                    }
#                                }},
#                         'en': {'type': 'text',
#                                'fields': {
#                                    "keywords": {
#                                        "type": "keyword"
#                                    }
#                                }
#                                }
#                     }
#                           },
#           "uri": {
#             "type": "keyword"
#           },
#           "identifier": {
#             "type": "keyword"
#           },
#           "scheme": {
#             "type": "keyword"
#           }
#         }
#       },
#       "descriptions": {'type': 'object', 'properties':
#                     {
#                         'cs': {'type': 'text',
#                                'fields': {
#                                    "keywords": {
#                                        "type": "keyword"
#                                    }
#                                }},
#                         'en': {'type': 'text',
#                                'fields': {
#                                    "keywords": {
#                                        "type": "keyword"
#                                    }
#                                }
#                                }
#                     }
#                           },
#       "locations": {
#         "type": "object",
#         "properties": {
#           "place": {
#             "type": "text"
#           },
#           "description": {'type': 'object', 'properties':
#                     {
#                         'cs': {'type': 'text',
#                                'fields': {
#                                    "keywords": {
#                                        "type": "keyword"
#                                    }
#                                }},
#                         'en': {'type': 'text',
#                                'fields': {
#                                    "keywords": {
#                                        "type": "keyword"
#                                    }
#                                }
#                                }
#                     }
#                           },
#           "point": {
#             "type": "object",
#             "properties": {
#               "lat": {
#                 "type": "double"
#               },
#               "lon": {
#                 "type": "double"
#               }
#             }
#           }
#         }
#       },
#       "references": {
#         "type": "object",
#         "properties": {
#           "reference_string": {
#             "type": "text"
#           },
#           "identifier": {
#             "type": "keyword"
#           },
#           "scheme": {
#             "type": "keyword"
#           }
#         }
#       },
#       "_created": {
#         "type": "date"
#       },
#       "_updated": {
#         "type": "date"
#       },
#       "$schema": {
#         "type": "keyword",
#         "index": False
#       },
#       "extensions": {
#         "type": "object",
#         "dynamic": False,
#         "enabled": False
#       },
#       "extensions_keywords": {
#         "type": "object",
#         "properties": {
#           "key": {"type": "keyword"},
#           "value": {"type": "keyword"}
#         }
#       },
#       "extensions_texts": {
#         "type": "object",
#         "properties": {
#           "key": {"type": "keyword"},
#           "value": {"type": "text"}
#         }
#       },
#       "extensions_longs": {
#         "type": "object",
#         "properties": {
#           "key": {"type": "keyword"},
#           "value": {"type": "long"}
#         }
#       },
#       "extensions_dates": {
#         "type": "object",
#         "properties": {
#           "key": {"type": "keyword"},
#           "value": {"type": "date"}
#         }
#       },
#       "extensions_booleans": {
#         "type": "object",
#         "properties": {
#           "key": {"type": "keyword"},
#           "value": {"type": "boolean"}
#         }
#       }
#     }
#   }
# }
