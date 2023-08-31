def ReadAndFix(file_path):
    """
    Read the state data from a file, clean it, and return a list of lists. Created by Adrian Pena
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
    Display the formatted state data. Created by Adrian Pena
    """
    for row in data_list:
        print('{0:2s} {1:20s} {2:15s} {3:10s}'.format(row[0], row[1], row[2], row[3]))

file_path = "/Users/adrianpena/Desktop/cat.txt"
state_list = ReadAndFix(file_path)
display_items(state_list)



