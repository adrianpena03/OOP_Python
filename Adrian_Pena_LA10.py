import json

# Step I: Read the CSV file and convert it into a list of dictionaries
Inlist = []
SList = []

with open('us_states.csv', 'r') as file:
    for line in file.readlines():
        s = line.strip().split(', ')
        state_info = {
            "abbrev": s[0],
            "name": s[1],
            "capital": s[2],
            "population": s[3]
        }
        SList.append(state_info)

# Print the list of dictionaries
for state in SList:
    print(f"{state['abbrev']} {state['name']} {state['capital']} {state['population']}")

# Step 2: Write SList to a JSON formatted file
jStringOut = json.dumps(SList)

with open('us_states.json', 'w') as json_file:
    json_file.write(jStringOut)

# Step 3: Show Json file
with open('us_states.json', 'r') as json_file:
    jStringIn = json_file.read()

print(jStringIn)

# Step 4: Read and convert
jsonStates = json.loads(jStringIn)

# Step 5: Print the names and population of states with a population > 5,000,000
for state in jsonStates:
    population = int(state['population'])
    if population > 5000000:
        print(f"{state['name']} - Population: {population}")
