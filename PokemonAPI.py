import requests
import sys
import json

POKEAPI_URL = "https://pokeapi.co/api/v2/"

def fetch_data(url): 
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ConnectionError(f"Error fetching data from {url}. Status code: {response.status_code}")

def fetch_ability(ability): 
    url = f"{POKEAPI_URL}ability/{ability}/"
    return fetch_data(url)

def fetch_species(pokemon_species):
    url = f"{POKEAPI_URL}pokemon-species/{pokemon_species}/"
    return fetch_data(url)

def fetch_pokemon_details(pokemon): # height and items
    url = f"{POKEAPI_URL}pokemon/{pokemon}"
    return fetch_data(url)

def jprint(obj):
    print(json.dumps(obj, indent = 4))


def main():
    pokemon_details = fetch_pokemon_details("bulbasaur")
    # jprint(pokemon_details)
    height = pokemon_details.get("height")
    print("height = ", height)
    items = pokemon_details.get("held_items")
    print("items = ", items)

    # species/known associates stuff
    species_name = pokemon_details.get("species").get("name")
    print("species = ", species_name)
    species_json = fetch_species(species_name)
    # jprint(species_json)
    varieties = species_json.get("varieties")
    print("varieties = ", end = "")
    jprint(varieties)   # this should be a list of dictionaries

if __name__ == "__main__":
    main()