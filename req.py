import requests
import json

# Simple script for fetching github user data with python requests.

credentials = ('srinivas-kini', 'my_password')  # login credentials
response = requests.get('https://api.github.com/user', auth=credentials)  # login with basic auth
print(response) # gives the HTTP status
resp_dict = response.json()  # convert the JSON response to a deserialized python dict
resp_json = json.dumps(resp_dict, indent=2)  # for pretty printing
print(resp_json)
