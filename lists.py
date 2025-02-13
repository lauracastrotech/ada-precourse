# February 12, 2025
# Programmer: Laura Castro
# Practice problems

def find_index_of_item(item, list_of_items):
    for i in range(len(list_of_items)):
        if item == list_of_items[i]:
            return i
    # item not found in list
    return -1

# Examples of working implementations:
def find_index_of_item(item, list_of_items):
    default = -1
    for i in range(len(list_of_items)):
        if list_of_items[i] == item:
            return i
    return default

def find_index_of_item(item, list_of_items):
    default = -1
    item_index = 0
    for current_item in list_of_items:
        if current_item == item:
            return item_index
        item_index += 1
    return default

# Using a while loop here isn't the most concise solution,
# but any time we can use a for loop, we can also use while loop!
def find_index_of_item(item, list_of_items):
    default = -1
    count = 0
    while count < len(list_of_items):
        if list_of_items[count] == item:
            return count
        count += 1
    return default

#####################################################################
def count_item_in_list(item, list_of_items):
    counter = 0
    for current_item in list_of_items:
        if current_item == item:
            counter += 1        
    return counter

# Examples of working implementations:

def count_item_in_list(item, list_of_items):
    count = 0
    for current_item in list_of_items:
        if current_item == item:
            count += 1
    return count

def count_item_in_list(item, list_of_items):
    count = 0
    for index in range(len(list_of_items)):
        if list_of_items[index] == item:
            count += 1
    return count

#####################################################################
def icecream_sundae(flavors, toppings):
    sundaes = []
    if len(flavors) == 0 or len(toppings) == 0:
        return sundaes
    else:
        for flavor in flavors:
            for topping in toppings:
                sundaes.append(f"{flavor} with {topping}")
    return sundaes

flavors = ["vanilla", "chocolate", "strawberry"]
toppings = ["whipped cream", "nuts", "a cherry"]
print(icecream_sundae(flavors, toppings))

# Examples of working implementations:
def icecream_sundae(flavors, toppings):
    result = []
    for flavor in flavors:
        for topping in toppings:
            pair = flavor + " with " + topping
            result.append(pair)
    return result

def icecream_sundae(flavors, toppings):
    result = []
    for flavor_index in range(len(flavors)):
        for topping_index in range(len(toppings)):
            pair = flavors[flavor_index] + " with " + toppings[topping_index]
            result.append(pair)
    return result
