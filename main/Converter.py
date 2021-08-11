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
            

def main():
    database_id = config.DATABASE_KEY
    parsed = NotionParser()
    print(parsed.get_database(database_id))


if __name__ == "__main__":
    main()



# Converter needs to parse Notion cURL and return a dictionary {type, children, text}
# TODO need to check child blocks if value == .header or .item or .children (either convert to lists or just throw a single check or check every time)