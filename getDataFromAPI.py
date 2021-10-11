import requests
import json
import os

if not os.path.exists("JSON/allPokemons.json"):
    response = json.loads(requests.get("https://pokeapi.co/api/v2/pokemon?limit=2000").text)
    with open('JSON/allPokemons.json', 'w') as fp:
        json.dump(response, fp)
    print("General file created!")
else:
    print("General file already exists!")

general_file = open('JSON/allPokemons.json',)
general_data = json.load(general_file)


total = len(general_data['results'])

pokemons = general_data['results']

print(pokemons[0])






