from ThingsHelper import ThingsModel
import requests
import json
import config

class NotionParser():
    base_url = 'https://api.notion.com'

    headers = {
        "Authorization": "Bearer " + config.INTEGRATION_KEY,
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }   

    @classmethod
    def get_database(self, database_id):
        database_url = self.base_url + '/v1/databases/' + database_id + '/query'
        response = requests.request("POST", database_url, headers=self.headers)
        if response.status_code != 200:
            return None
        else:
            return response.json()

    # method that produces a list of pages to select from
    # NOTE: this method is for selecting a full set of data later on, API requires second call to get page contents
    # PARAM json_database: JSON format of Notion database to be parsed
    # RETURN list of table names
    @classmethod
    def extract_pages_from_json(self, json_database):
        pass
            
    # method that get the contents of a page from a database
    # PARAM page_id: string used to reference a specific page from API
    # RETURN page_content: JSON dictionary of page contents
    @classmethod
    def get_page_contents(self, page_id):
        pass

def main():
    database_id = config.DATABASE_KEY
    parsed = NotionParser()

    # pretty printing
    to_format = parsed.get_database(database_id)
    print(json.dumps(to_format, indent=4))


if __name__ == "__main__":
    main()



# Converter needs to parse Notion cURL and return a dictionary {type, children, text}
# TODO need to check child blocks if value == .header or .item or .children (either convert to lists or just throw a single check or check every time)