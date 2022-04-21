import requests

endpoint = "http://localhost:8000/api/medadmin/"

response = requests.get(endpoint)
print(response.json())  #prints out the json response of an api