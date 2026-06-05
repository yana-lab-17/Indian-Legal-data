import requests

TOKEN = "e97ad0a4ce243557c87589eda2cf82f3d4a8ac50"

headers = {
    "Authorization": f"Token {TOKEN}"
}

url = "https://api.indiankanoon.org/search/?formInput=consumer protection&pagenum=0"

response = requests.post(url, headers=headers)

print("Status Code:", response.status_code)
data=response.json()
print(data.keys())
print(type(data))
print(type(data["categories"]))
print(type(data["categories"][0]))  
print(data["categories"][0])
print(len(data["categories"]))
print(len(data["docs"]))
print(len(data["found"]))
print(data["docs"])