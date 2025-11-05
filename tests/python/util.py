# This script stores all the functions necessary to create elements like lists, sets or arrays
# full with specified data

# Generate an unsorted list of numbers with a missing value
def get_unsorted_list_with_missing_value(size, missing_value):
    list_test = set(range(1, size + 1))
    list_test.remove(missing_value)
    return list(list_test)

# Fill a list of numbers with values in a given range
def fill_list_with_range(size, final, first=1):
    list_values = []
    max_val = final - first + 1
    for i in range(size):
        if(max_val != 0):
            list_values.append((i % max_val) + first)
        else:
            list_values.append(0)
    return list_values

# Return a string with specified characters
def create_string(size, list_of_characters):
    string = ""
    for i in range(size):
        string = string + list_of_characters[i%len(list_of_characters)]
    return string

# Create a aplindome from a string
def create_palindome_string(original):
    string = ""
    for i in range(len(original)):
        string = string + original[i]
    for i in range(len(original)-1, -1, -1):
        string = string + original[i]
    return string

# Return a sorted list with values in a range
def fill_sorted_list_with_range(size, final, first=1):
    list_v =  fill_list_with_range(size, final, first)
    list_v.sort()
    return list_v

# Return a list with lists of pairs of numbers
def fill_array_of_arrys(max_val, min_val = 0):
    if min_val < 0:
        min_val*= -1
    result = []
    for i in range(max_val, min_val -1, -1):
        result.append([-i,i])
    return result

