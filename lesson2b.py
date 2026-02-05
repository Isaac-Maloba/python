# TUPLE
# a tuple is an immutable type of a list i.e it cannot change
# To introduce a tuple, we use the parenthesis

counties = ("Nairobi", "Bungoma", "Mombasa", "Nakuru", "Narok", "Kisumu")
print(counties)
print(type(counties))

# slicing of tuples
print(counties[3:])

# accessing the items of a tuple by use of the indexes
print(counties[4])

# Below will generate an error
# Attribute error
counties.append("Machakos")