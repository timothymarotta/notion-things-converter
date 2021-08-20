import unittest
import json
from Converter import NotionParser

class NotionParserTest(unittest.TestCase):
    parser = NotionParser()

    def test_get_database(self):
        pass

    # uses data from MockDatabase.json
    def test_extract_pages_from_json(self):
        with open('./main/MockDatabase.json',) as inFile:
            temp = inFile.read()
            data = json.loads(temp)
            

        with open('./main/ExtractPagesExpected.json',) as inExpected:
            temp = inExpected.read()
            expected = json.loads(temp)

        self.assertEqual(expected, self.parser.extract_pages_from_json(data))

    def test_get_page_contents(self):
        pass