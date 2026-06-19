import requests
from bs4 import BeautifulSoup

TOKEN = "e97ad0a4ce243557c87589eda2cf82f3d4a8ac50"

headers = {
    "Authorization": f"Token {TOKEN}"
}
'''
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
print(len(data["docs"]))
print(data["docs"][0])'''
doc_id = 1891987

url = f"https://api.indiankanoon.org/doc/{doc_id}/"

response = requests.post(
    url,
    headers=headers
)

print(response.status_code)

document = response.json()

print(document.keys())
print(type(document["doc"]))
print(document["doc"][:1000])
html = document["doc"]

soup = BeautifulSoup(html, "html.parser")

clean_text = soup.get_text(separator=" ", strip=True)

print(clean_text[:2000])