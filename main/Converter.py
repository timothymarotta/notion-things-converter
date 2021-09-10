from ThingsHelper import ThingsModel
import requests
import json
import config

class NotionParser():
    base_url = 'https://api.notion.com/'
    version_no = 'v1/'

    headers = {
        'Authorization': 'Bearer ' + config.INTEGRATION_KEY,
        'Content-Type': 'application/json',
        'Notion-Version': '2021-08-16'
    }   

    @classmethod
    def get_database(self, database_id):
        database_url = self.base_url + self.version_no + 'databases/' + database_id + '/query'
        response = requests.request('POST', database_url, headers=self.headers)
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
        results_only = json_database['results']
        to_return = {'page_titles':[]}
        for page in results_only:
            duo = {}
            # TODO these really should be search algorithms instead of hard coded, i just dont feel like it right not
            duo['id'] = page['id']
            duo['plain_text'] = page['properties']['Name']['title'][0]['plain_text']
            to_return['page_titles'].append(duo)
        return to_return
            
    def select_page(self, page_set):
        print('Please select a template number:')
        page_list = page_set['page_titles']
        for i in range(0, len(page_list)):
            page_pair = page_list[i]
            print(str(i+1) + ': ' + page_pair['plain_text'])
        choice = int(input())
        # TODO handle non-integer answers
        # TODO handle out of range answers
        return page_list[choice - 1]['id']

    # method that get the contents of a page from a database; NOTE THIS IS NOT RETRIEVING THE PAGE, JUST ITS CONTENTS
    # PARAM page_id: string used to reference a specific page from API
    # RETURN page_content: JSON dictionary of page contents
    @classmethod
    def get_page_contents(self, page_id):
        page_url = self.base_url + self.version_no + 'blocks/' + page_id + '/children'
        print(page_url)
        response = requests.request('GET', page_url, headers=self.headers)
        # if response.status_code != 200:
        #     return type(response)
        # else:
        #     return response.json()
        return response.json()

def main():
    database_id = config.DATABASE_KEY
    parsed = NotionParser()

    # pretty printing
    to_format = parsed.get_database(database_id)
    pages = parsed.extract_pages_from_json(to_format)
    selected = parsed.select_page(pages)
    template = parsed.get_page_contents(selected)
    print(template)


if __name__ == "__main__":
    main()



# Converter needs to parse Notion cURL and return a dictionary {type, children, text}
# TODO need to check child blocks if value == .header or .item or .children (either convert to lists or just throw a single check or check every time)