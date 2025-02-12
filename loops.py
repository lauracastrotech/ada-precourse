# def print_ten(word):
#     final_string = ""
#     for num in range(1, 11):
#         final_string += str(num)+ " "+ word+ " "
#     return final_string

# print(print_ten("hello"))

# # Ada examples of working implementation
# def print_ten(word):
#     count = 1
#     result = ""
#     while count < 11:
#         result += str(count)
#         result += " "
#         result += word
#         result += " "
#         count += 1

#     return result

# def print_ten(word):
#     result = ""
#     for i in range(1, 11):
#         result += str(i) + " "
#         result += word + " "
#     return result

def print_multiple(word, amount):
    result = ""
    for i in range(1, amount + 1):
        if i == amount:
            result += str(i)
            result += " "
            result += word
        else:
            result += str(i)
            result += " "
            result += word
            result += " "
    return result

#Two examples of working implementations:

def print_multiple(word, amount):
    count = 1
    result = ""
    while count < amount + 1:
        if count > 1:
            result += " "
        result += str(count)
        result + " "
        result += word
        count += 1

    return result

def print_multiple(word, amount):
    result = ""
    for i in range(1, amount + 1):
        if i > 1:
            result += " "
        result += str(i) + " "
        result += word
    return result