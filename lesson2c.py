# A dictionary is a data type that stores data in terms of key-value pairs
# A dictionary is introduced by the use of carrying braces/ brackets {}
# The values stored inside of a dictionary can be of any data type
# To access the values in a dictionary, we use the keys

phonebook = {
    "Benson" : "+254789763526",
    "Mary" : "+254798367274",
    "John" : "+254127846732"
}

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

print('=====================')
player = {
    "Name" : "Lionel Messi",
    "Age" : 40,
    "Teams" : ["PSG", "Barcelona", "Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "phone" : (254788888, 254799999, 25433333)
    }
}

print(player)
print(player["Teams"][1])

# Research on if...else statements in python
print(player["more"]["phone"][1])