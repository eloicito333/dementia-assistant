from dotenv import load_dotenv
load_dotenv()

import requests
import os
from  program_settings import verbose

class SpokenDataDB:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
    
    def post_document(self, document):
        if verbose: print("posting document to db: ", document)
        response = requests.post(self.url+"/spokenData/document", json=document, headers=self.headers)
        
        return response.json()
    
    def search_document(self, query):
        response = requests.post(self.url+"/spokenData/search", json=query, headers=self.headers)
        
        return response.json()


class APIHelper:
    def __init__(self, url, api_key):
        self.api_url = url
        self.url= url + "/api"
        self.api_key = api_key

        self.headers = {'Authorization': api_key}

        self.spoken_data_db = SpokenDataDB(url=self.url, headers=self.headers)

api_helper = APIHelper(url=os.getenv("INTERNAL_API_URL"), api_key=os.getenv("INTERNAL_API_KEY"))