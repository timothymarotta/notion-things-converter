import unittest
import json
from Converter import NotionParser

class NotionParserTest(unittest.TestCase):
    parser = NotionParser()

    def test_get_database(self):
        pass

    # uses data from MockDatabase.json
    def test_extract_pages_from_json(self):
        inFile = open('MockDatabase.json')
        data = json.loads(inFile)

        inExpected = open('ExtractPagesExpected.json')
        expected = json.loads(inExpected)

        self.assertEqual(expected, self.parser.extract_pages_from_json(data))

    def test_get_page_contents(self):
        pass