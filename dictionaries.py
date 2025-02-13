# February 13, 2025
# Programmer: Laura Castro
# Practice problems

def get_value_from_dictionary(dict, key):
    for k in dict:
        if k == key:
            return dict[key]  
    return None

# Some example solutions:
def get_value_from_dictionary(dict, key): # This is Ada's preferred solution
    if key not in dict:
        return None
	        
    return dict[key]
    
def get_value_from_dictionary(dict, key):
    if key in dict:
        return dict[key]

    return None
#####################################################################
def dict_counter(dict, key):
    if key not in dict:
        dict[key] = 1
    else:
        dict[key] += 1
    return dict

#An example solution:

# Example 1
def dict_counter(dict, key):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

    return dict

# Example 2
def dict_counter(dict, key):
    if key not in dict:
        dict[key] = 1
    else:
        dict[key] += 1

    return dict
#####################################################################
def build_a_dictionary(keys, values):
    new_dict = {}
    if not len(keys) == len(values):
        return None
    else: 
        for idx in range(len(keys)):
            new_dict[keys[idx]] = values[idx]
            print(keys[idx])
            print(values[idx])
            print(new_dict)
    return new_dict

# An example solution
def build_a_dictionary(keys, values):
    if len(keys) != len(values):
        return None
      
    result = {}
    for index in range(len(keys)):
        result[keys[index]] = values[index]
    return result