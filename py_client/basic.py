import requests

endpoint = "http://localhost:8000/"

response = requests.get(endpoint)
print(response.text)  #prints out the source code of a website