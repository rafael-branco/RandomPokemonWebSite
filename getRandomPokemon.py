import json
import mysql.connector
from time import sleep
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/getRandomPokemon.py', methods=['POST'])
def process():
    return jsonify({'teste': 'meu teste deu certo :D'})
 
if __name__ == '__main__':
    app.run(debug=True)