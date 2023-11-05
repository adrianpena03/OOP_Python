"""
We identified some interesting things happening in our environment and were able to pick out
several abilities that were used by a suspicious actor (Pokémon). When an alert comes in with
the relevant abilities observed, we need to be able to find who may have been involved by
figuring out:

- which Pokémon could have used the ability,
- anyone close to them (within the same “Species”) that we can ask about their alibi,
- any items they might be stowing that we should look out for, and
- some identifiable information about the suspect, specifically whether they are the tallest
  or the shortest of the group of Pokémon who can use each ability

If there aren’t any Pokémon in the Species beyond the suspect themselves, leave the
"known_associates" list blank so we don’t waste investigation time. For each input ability,
determine the tallest and shortest Pokémon and note them as such in their record.
Use the v2 PokéAPI (https://pokeapi.co/docs/v2) to gather the required information and return it
in the below output format so that it may be ingested by another part of the pipeline. This
assignment should take 1-2 hours. Leave enough time to consider polish and error handling in
your code.
How to submit your exercise: Send in a zip file containing your submission. Your program
should run as follows:
./pokedex abilityA abilityB ... abilityZ

Example input:
./pokedex stench volt-absorb
"""

import requests

POKEAPI_URL = "https://pokeapi.co/api/v2/ability/"

# def fetch_pokemon_info(ability):
response = requests.get(f"{POKEAPI_URL}")
if response.status_code != 200:
    print ("Error, status code not 200.")

print(response.status_code)
data = response.json()
print(data)


