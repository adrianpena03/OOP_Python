def ReadAndFix(file_path):
    """
    Read the state data from a file, clean it, and return a list of lists.
    """
    clean_content = []
    with open(file_path, "r") as f:
        for line in f:
            x = line.strip().replace(";", ",").replace("\n", "")
            clean_row = [item.strip() for item in x.split(',')]
            clean_content.append(clean_row)
    return clean_content

def display_items(data_list):
    """
    Display the formatted state data with centered column headers.
    """
    headers = ["Abbrev.#", "Name", "Capital", "Population"]
    print('{0:^8s} {1:^20s} {2:^15s} {3:^10s}'.format(*headers))
    print('=' * 8, '=' * 20, '=' * 15, '=' * 10)  # Separator line

    for row in data_list:
        print('{0:8s} {1:20s} {2:15s} {3:10s}'.format(row[0], row[1], row[2], row[3]))

def buildDict(stateList):
    """
    Build a dictionary from the state list with state abbreviation as key and state info as value.
    """
    state_dict = {}
    for row in stateList:
        state_abbreviation = row[0]
        state_info = [row[1], row[2], row[3]]
        state_dict[state_abbreviation] = state_info
    return state_dict

def writeFile(state_dict):
    """
    Create an output text file and write each state item from the dictionary in comma-separated format.
    """
    with open("IT209_A1output.txt", "w") as output_file:
        for state_abbreviation, state_info in state_dict.items():
            state_data = ",".join(state_info)
            output_file.write(state_data + "\n")

def writeFile(state_dict):
    """
    Create an output text file and write each state item from the dictionary in comma-separated format.
    """
    with open("IT209_A1output.txt", "w") as output_file:
        for state_abbreviation, state_info in state_dict.items():
            state_data = ",".join(state_info)
            output_file.write(state_data + "\n")
            

file_path = "/Users/adrianpena/Desktop/cat.txt"
state_list = ReadAndFix(file_path)
display_items(state_list)
state_dict = buildDict(state_list)
writeFile(state_dict)

