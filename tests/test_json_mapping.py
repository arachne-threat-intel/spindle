import os
import json
import requests
import unittest

THREAD_COUNTRY_CONF = 'https://raw.githubusercontent.com/arachne-threat-intel/' \
                      'thread/main/threadcomponents/conf/countries-iso2.json'


class TestJSONMapping(unittest.TestCase):
    """A test case for the JSON mappings file."""
    JSON_MAPPING_FILENAME = 'cta_names_mappings.json'
    loaded_json = None

    @classmethod
    def setUpClass(cls):
        cls.assertTrue(os.path.isfile(cls.JSON_MAPPING_FILENAME), 'JSON mapping file not found.')
        with open(cls.JSON_MAPPING_FILENAME) as json_mapping_opened:
            cls.loaded_json = json.load(json_mapping_opened)

    def test_country_values(self):
        """Tests whether country codes within the JSON mapping file are valid."""
        countries = requests.get(THREAD_COUNTRY_CONF).json()
        country_codes = [c['alpha-2'].upper() for c in countries]
        for group, entry in self.loaded_json.items():
            entry_countries = entry.get('countries', [])
            for entry_country in entry_countries:
                error_msg = "Country '%s' under '%s' is not a valid country code." % (entry_country, group)
                self.assertTrue(entry_country.upper() in country_codes, msg=error_msg)
