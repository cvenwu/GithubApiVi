import requests
import json
URL = "https://api.github.com/users/sivanWu0222"
response = requests.get(URL)
print(type(response))
response_dict = response.json()
print(response_dict)
