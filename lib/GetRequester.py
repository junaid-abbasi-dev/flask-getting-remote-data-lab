import requests
import json

class GetRequester:
    # URL for api 
    # "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    # initialize class with url instance
    def __init__(self, url):
        self.url = url
    # get response using requests library
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
    # loads and converts the data from api 
    def load_json(self):
        response = json.loads(self.get_response_body())
        return response

URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
results = GetRequester(URL).get_response_body()
formatted_results = GetRequester(URL).load_json()
print("Raw data:")
print(results)
print("Formatted data: ")
print(formatted_results)