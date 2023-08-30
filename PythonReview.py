# IT 209 - Python Review - Demo 1

abrev = "VA"

states1 = [["AL", "Alabama", "Montgomery"],
        ["AL", "Alaska", "xxxxxx"],
        ["CA", "California", "Sacramento"],
        ["MD", "Maryland", "Baltimore"],
        ["VA", "Virginia", "Richmond"]
        ]

states2 = [["CO", "Colorado", "Denver"],
        ["NC", "North Carolina", "Raleigh"],
        ["ND", "North Dakota", "ND_Cap"],
        ["ID", "Idaho", "ID_Cap"],
        ]

def StateName(abrev):
    """Accepts state abbreviation, returns full name of state"""
    for s in states1:
        if abrev == s[0]:
            return s[1]
    return "Not Found."
# print(StateName(abrev))

# for i in range(len(states)):
#     print(i)
#     print(states[i])

# fname = ("/Users/adrianpena/Desktop/Cat.txt", "r")
# r = open(fname)
# #do stuff
# r.close() # have to close to see changes


# with open("/Users/adrianpena/Desktop/Cat.txt", "a") as f: # fix
#     f.write("7, Greeetings!")
#     f.write("8, Welcome!")
#     for line in f:
#         f.strip("\n")
#     print(f.readlines)

# def validate_phone_number(phone_number):
#     digits_count = 0

#     for char in phone_number:
#         if char.isdigit():
#             digits_count += 1

#     if digits_count == 10:
#         return True
#     else:
#         return False
    
# phone_number = "(555) 456 - 798"

# print(validate_phone_number(phone_number))

