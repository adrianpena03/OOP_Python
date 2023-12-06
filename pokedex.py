import requests
import sys
import json

POKEAPI_URL = "https://pokeapi.co/api/v2/"

def jprint(obj):
    print(json.dumps(obj, indent = 4))

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
    url = f"{POKEAPI_URL}pokemon/{pokemon}"
    return fetch_data(url)

def get_tallest_shortest(species_name):
    url = f"{POKEAPI_URL}pokemon-species/{species_name}/"
    species_data = fetch_data(url)
    
    tallest = False
    shortest = False
    if "tallest" in species_data.get("varieties", []):
        tallest = True
    elif "shortest" in species_data.get("varieties", []):
        shortest = True
    
    return tallest, shortest

def main():
    if len(sys.argv) < 2:
        print("Usage: ./pokedex abilityA abilityB ...")
        sys.exit(1)

    abilities = sys.argv[1:]

    results = {}

    for ability in abilities:
        print(f"\nProcessing ability: {ability}")
        results_for_current_ability = []

        # Fetch data for the current ability
        ability_data = fetch_ability(ability)

        for pokemon in ability_data["pokemon"]:
            pokemon_name = pokemon["pokemon"]["name"]

            # Fetch Pokemon details
            pokemon_details = fetch_pokemon_details(pokemon_name)

            # Fetch species information
            species_name = pokemon_details["species"]["name"]
            species_data = fetch_species(species_name)

            # Fetch known associates
            known_associates = [assoc["pokemon"]["name"] for assoc in ability_data["pokemon"] if assoc["pokemon"]["name"] != pokemon_name]

            # Fetch tallest and shortest information
            tallest, shortest = get_tallest_shortest(species_name)

            # Placeholder for height and items
            height = pokemon_details.get("height")
            items = pokemon_details.get("held_items", [])

            # Append data to the results list
            results_for_current_ability.append({
                "name": pokemon_name,
                "known_associates": known_associates,
                "items": items,
                "tallest": tallest,
                "shortest": shortest
            })

        # Store results for the current ability
        results[ability] = results_for_current_ability

    # Print the final results
    jprint(results)

if __name__ == "__main__":
    main()