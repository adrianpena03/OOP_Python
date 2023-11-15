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

def fetch_pokemon_details(pokemon): 
    url = f"{POKEAPI_URL}pokemon/{pokemon}/"
    return fetch_data(url)

def get_tallest_shortest(pokemon_list):
    tallest = max(pokemon_list, key=lambda x: x['height'])
    shortest = min(pokemon_list, key=lambda x: x['height'])
    for p in pokemon_list:
        p['tallest'] = p['name'] == tallest['name']
        p['shortest'] = p['name'] == shortest['name']
    return pokemon_list

def main():
    abilities = sys.argv[1:]
    result = {}

    for ability in abilities:
        ability_data = fetch_ability(ability)
        pokemon_list = []

        for pokemon in ability_data['pokemon']:
            pokemon_name = pokemon['pokemon']['name']
            species_data = fetch_species(pokemon_name)
            pokemon_details = fetch_pokemon_details(pokemon_name)
            
            known_associates = [variety['pokemon']['name'] for variety in species_data.get('varieties', [])]
            
            pokemon_info = {
                'name': pokemon_name,
                'known_associates': known_associates,
                'items': [item['item']['name'] for item in pokemon_details.get('held_items', [])],
                'height': pokemon_details.get('height', 0)
            }

            pokemon_list.append(pokemon_info)

        result[ability] = get_tallest_shortest(pokemon_list)

    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
