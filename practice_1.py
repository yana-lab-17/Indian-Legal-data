import requests as req
res=req.get("https://pokeapi.co/api/v2/pokemon")
print(res.status_code)
data=res.json()
print(data)
print(len(data))
print(type(data))
print(data.keys())
print(data["count"])
print(data["previous"])
result=data["results"]
for i in result:
    print(i["url"])
print("longest name")
long_name=""
for i in result:
    if(len(i["name"])>len(long_name)):
        long_name=i["name"]
print(long_name)
print("Name starts with letter b")
cnt=0
for i in result:
    if(i["name"].startswith("b")):
        print(i["name"])
        cnt+=1
print(cnt)