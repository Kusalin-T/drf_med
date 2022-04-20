import requests

endpoint = "http://localhost:8000/api/medadmin/1/"

response = requests.get(endpoint)
print(response.json())  #prints out the source code of a website