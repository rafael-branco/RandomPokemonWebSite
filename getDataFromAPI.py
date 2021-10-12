import requests
import json
import os
import time

if not os.path.exists("JSON/allPokemons.json"):
    response = json.loads(requests.get("https://pokeapi.co/api/v2/pokemon?limit=2000").text)
    with open('JSON/allPokemons.json', 'w') as fp:
        json.dump(response, fp)
    print("General file created!")
    response.close()
else:
    print("General file already exists!")

general_file = open('JSON/allPokemons.json',)
general_data = json.load(general_file)


total = len(general_data['results'])

pokemons = general_data['results']

for p in pokemons:
    
    temp_url = p["url"]
    folder = temp_url.split("/")[-2]

    if not os.path.exists("JSON/Pokemons/"+ folder +".json"):
        rsp = requests.get(str(temp_url)).json()
        with open("JSON/Pokemons/"+ folder +".json", 'w') as fp:
            json.dump(rsp, fp)
            print(folder+" file created!")
            time.sleep(5)
    else:
        print(folder + " file already exists!")
    








