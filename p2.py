#import requests

# url= "https://official-joke-api.appspot.com/random_joke"

# response= requests.get(url)


# if response.status_code == 200:
#     data = response.json()
# else:
#     print("API request failed")
# ##without checking this with the status code the program may crash if it has any issue 
# print("Joke:")
# print(data["setup"])
# print(data["punchline"])


#2
# import requests as req

# try:
#     res = req.get("https://pokeapi.co/api/v2/pokemon")

#     res.raise_for_status()

#     data = res.json()

#     print(data["count"])

# except Exception as e:
#     print("Error Something went wrong:", e)


#3-getting inputs from the user 
# import requests as req

# name = input("Enter Pokemon name: ")

# url = f"https://pokeapi.co/api/v2/pokemon/{name}"

# res = req.get(url)

# data = res.json()

# print("Name:", data["name"])
# print("Height:", data["height"])
# print("Weight:", data["weight"])

#4
# import requests as req
# import json

# res = req.get("https://pokeapi.co/api/v2/pokemon")

# data = res.json()
# print (data)
# print(json.dumps(data, indent=4))

#dumps- it converts the normal string into json formatted string 
# where in normal it includes everything like (count , next ,previous etc)
# which is hard to read as a user ,soo we use json formatted (dump) with
# indent- spaces and leaves a line as default 


# 5th FUNCTIONS

import requests as req

def get_pokemon(name):

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    res = req.get(url)

    return res.json()

data = get_pokemon("pikachu")

print(data["name"])
print(data["height"])
print(data["weight"])