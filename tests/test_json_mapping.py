import os
import json
import unittest


class TestJSONMapping(unittest.TestCase):
    """A test case for the JSON mappings file."""
    JSON_MAPPING_FILENAME = 'cta_names_mappings.json'

    def test_valid_json(self):
        self.assertTrue(os.path.isfile(self.JSON_MAPPING_FILENAME), 'JSON mapping file not found.')
        with open(self.JSON_MAPPING_FILENAME) as json_mapping_opened:
            json.load(json_mapping_opened)
