from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

def show_pet(index):
    pet = pets[index]  # Assuming `pets` is the list of pet data
    return render_template('show_pet.html', pet=pet)