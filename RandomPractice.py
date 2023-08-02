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