nums = [1, 2, 3, 4, 5]
print(*nums)

# The ' * ' symbol unpacks whatever is inside the [ ]

def order_pizza(size, *args, **kwargs): # kwargs handles keyword arguments, output is type dict
    print(f"Ordered a {size} pizza with the following toppings:")
    for topping in args:
        print(f"- {topping}")
    print(f"\nDetails of the order are:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

order_pizza('large', 'pepperoni', 'pineapple', delivery=True, tip=5)


# Syntactic Sugar
newI = [print(i*2) for i in range(10)]

#-------------------------------------------------------
# ENUMERATE PROBLEMS

# Problem: Find all indices of all ocurrances of a specific element in a list.
# write a function called 'find_indices' that takes two parameters, ' my_list ' (list of elements)
# and ' target ' (element to find in list) and retuns
# a list containing the indices of all occurrences of the target element in the input list.

def find_indices(my_list, target):
    new_lis = []
    for index, value in enumerate(my_list):
        if value == target:
            new_lis.append(index)
    return new_lis

my_list = [1, 2, 3, 4, 2, 5, 2]
target = 2
result = find_indices(my_list, target)
print(result)


# Problem: Create a Letter Pyramid
# Write a function called letter_pyramid that takes a string as input and prints a letter pyramid. 
# Each level of the pyramid should consist of the letters from the input 
# string up to the current position.


def letter_pyramid(word):
    # Your code here
    pass

# Test the function
letter_pyramid("PYTHON")

# You can use the enumerate function to iterate over the characters in the word along with their indices.
# Think about how to concatenate the letters for each level of the pyramid.

# ------------------------

lis = [2, 3, 4, 5, 6]

my_iterator = iter(lis)

while True:
    try:
        element = next(my_iterator)
        print(element)
    except StopIteration:
        print('end of list')
        break