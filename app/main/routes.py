from flask import Blueprint, render_template
import requests

main = Blueprint("main", __name__)

@main.route("/")
def index():
    data = requests.get("https://pokeapi.co/api/v2/pokemon?limit=50").json()
    return data
