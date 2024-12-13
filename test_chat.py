import requests

url = "http://127.0.0.1:5000/chat"
data = {"message": "Hello, Einstein!"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.json())
