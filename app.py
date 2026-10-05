from flask import Flask, render_template, abort
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql

app = Flask(__name__)

pokemons = [
        { "id": 1, "name": "Charmander", "type": "Fire", "evolution": "Charmeleon", "evolution_level": 16 },
        { "id": 2, "name": "Squirtle", "type": "Water", "evolution": "Wartortle", "evolution_level": 16 },
        { "id": 3, "name": "Bulbasaur", "type": "Grass", "evolution": "Ivysaur", "evolution_level": 16 }
    ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pokemons')
def pokemon_list():
    return render_template('pokemons.html', pokemons_list=pokemons)

@app.route("/pokemons/<int:pokemon_id>")
def pokemon(pokemon_id):
    for pokemon in pokemons:
        if pokemon["id"] == pokemon_id:
            return render_template("pokemon.html", pokemon=pokemon)
    abort(404)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)