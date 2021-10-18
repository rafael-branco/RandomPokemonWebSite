import requests
import json
import os
import time
import mysql.connector

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

mydb = mysql.connector.connect(user=mysql_data['mysql_info']['user'],
                              password=mysql_data['mysql_info']['password'],
                              host=mysql_data['mysql_info']['host'],
                              database=mysql_data['mysql_info']['database'])
db_cursor = mydb.cursor()

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
        pokefile = open("JSON/Pokemons/" + folder + ".json", )
        pokemon = json.load(pokefile)
        sql = "INSERT IGNORE INTO pokemon (id, name, type01, type02, sprite) VALUES (%s, %s, %s, %s, %s)"
        val = (pokemon['id'], pokemon['name'], pokemon['type01'], pokemon['type02'],  pokemon['sprite'])
        db_cursor.execute(sql, val)
        mydb.commit()







    








