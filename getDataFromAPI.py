import requests
import json
import os
import time
import mysql.connector
from time import sleep

if not os.path.exists("JSON/allPokemons.json"):
    response = json.loads(requests.get("https://pokeapi.co/api/v2/pokemon?limit=2000").text)
    with open('JSON/allPokemons.json', 'w') as fp:
        json.dump(response, fp)
    print("General file created!")
    response.close()
else:
    print("General file already exists!")

mysql_file = open('JSON/mysql.json',)
mysql_data = json.load(mysql_file)

mydb = mysql.connector.connect(user=mysql_data['mysql_info'][0]['user'],
                              password=mysql_data['mysql_info'][0]['password'],
                              host=mysql_data['mysql_info'][0]['host'],
                              database=mysql_data['mysql_info'][0]['database'])
db_cursor = mydb.cursor()

general_file = open('JSON/allPokemons.json',)
general_data = json.load(general_file)


total = len(general_data['results'])

pokemons = general_data['results']

qtd = []

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
        #print(folder + " file already exists!")
        pokefile = open("JSON/Pokemons/" + folder + ".json", )
        pokemon = json.load(pokefile)
        sql = "INSERT IGNORE INTO pokemon (id, name, type01, type02, sprite) VALUES (%s, %s, %s, %s, %s)"
        count = 0
        types = []
        for type in pokemon['types']:
            types.append(type['type']['name'])

        if len(types) == 1:
            types.append(None)

        val = (pokemon['id'], pokemon['name'], types[0], types[1], pokemon['sprites']['other']['official-artwork']['front_default'])
        db_cursor.execute(sql, val)
        mydb.commit()
        pokefile.close()

print("Done!")





    








