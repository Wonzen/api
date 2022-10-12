import requests

get = requests.get("http://127.0.0.1:3000/api/users")
print(get.json())

