# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Test jsonschema validation."""

import json

from invenio_jsonschemas import current_jsonschemas
from invenio_records.api import Record


def get_schema():
    """This function loads the given schema available"""

    try:
        with open('../test_module/jsonschemas/test/test-v1.0.0.json', 'r') as file:
            schema = json.load(file)
    except:
        with open('./tests/test_module/jsonschemas/test/test-v1.0.0.json', 'r') as file:
            schema = json.load(file)

    return schema

def test_json(app):
    """Test of json schema with app."""
    # TODO: this needs to be rewritten to resolve schema $refs before testing
    # schema = app.extensions['invenio-records']
    #
    # data = json.loads('{"these": {"title" : {"cs": "jej", "en": "yay"}, "abstract":{"cs-cz": "jej"}}}')
    # schema.validate(data, get_schema())
    #
    # data = json.loads('{"subjects":[{"subject": {"cs":"neco", "en-us":"neco jinyho"}}]}')
    # schema.validate(data, get_schema())
    #
    # data = json.loads('{"locations":[{"description": {"cs":"neco", "en-us":"neco jinyho"}, "place": "string"}]}')
    # schema.validate(data, get_schema())

