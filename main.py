import requests as req
res=req.get("https://jsonplaceholder.typicode.com/users")
data=res.json()
for i in data:
    print(i["name"])

'''response = requests.get(
    "https://pokeapi.co/api/v2/pokemon"
)

data = response.json()
print(data)
for p in data["results"]:
    print(p["name"])
    '''
