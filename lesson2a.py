# Python Lists
# A list is a collection of items that are ordered in a certian way
# Alist is introduced by the use of the square brackets []
# The items of a list are stored inside of indexes. In programming, we start counting from index zero (0)
# Alist is mutable i.e The contents of a list can be changed

cars = ["BMW", "Benz", "Hiace", "Toyota", "Mazda", "McLaren", "Bentley"]
numbers = [5, 18, 67]

print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print(numbers)
print(type(numbers))
print("The car on index 4 is:", cars[4])

# List slicing - This is creating a list from a given larger list
print(cars[4:])

# Printing from index 0 to 3
print(cars[:4])

# Printing from Hiace to McLaren
print(cars[2:5])

# List Mutability
# we use the function append to add an item at the end of a list
cars.append("Volkswagon")
print(cars)
cars.append("Ferrari")
print(cars)
print(cars[3:])

# we use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

# Deleting a specific item from the list
cars.pop(4)
print(cars)

del cars[0]
print(cars)


# we can use an index to add items to a list
cars[5] = "Buggati"
print(cars)

# We can use the sort function to sort our items in alphabetical order
cars.sort()
print(cars)

# Reverse sorting
cars.sort(reverse=True)
print(cars)