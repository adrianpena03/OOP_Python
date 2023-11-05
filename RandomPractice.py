import random


def orderIceCream(flavors, toppings, sizes):
    f = int(random.randint(0,len(flavors)-1))
    t = int(random.randint(0,len(toppings)-1))
    s = int(random.randint(0,len(sizes)-1))
    return f, t, s

icecream = {
    "flavors": ["vanilla", "chocolate", "strawberry"],
    "toppings": ["sprinkles", "hot fudge", "peanuts"],
    "sizes": ["small", "medium", "large"]
}

icecream["flavors"].append("Cookie Dough")

lis = []

for key, value in icecream.items():
    lis.append(value)

for i in range(5):
    order = orderIceCream(icecream["flavors"], icecream["toppings"], icecream["sizes"])
    f = icecream["flavors"][order[0]]
    t = icecream["toppings"][order[1]]
    s = icecream["sizes"][order[2]]
    print("Order " + str(i+1) + ": Flavor: " + f + ", Topping: " + t + ", Size: " + s)

# # Given a string str. You are allowed to delete only some contiguous characters if all the characters are the same in a single operation. The task is to find the minimum number of operations required to completely delete the string. 

# Examples:

# Input: str = “abcddcba” 

# Output: 4 Delete dd, then the string is “abccba” Delete cc, then the string is “abba” Delete bb, then the string is “aa” Delete aa, then the string is null. 

# Input: str = “abc” 

# Output: 3 

