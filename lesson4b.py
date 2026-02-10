# Loops -> Sometimes we may need to doa piece of work a number of repeate times and in such cases, we may use loops
# A loop is a control structure that allows us to execute a block of code repeatedly until a certain condition is met
# There are 2 types of loops in python i.e FOR loop and WHILE loop
# Below is the syntax for the for loop in python
"""
for variable in range(n)
    # block of code to be executed
"""

for greeting in range(500):
    print("Hello Moses", greeting) # what is happening here? why does the "greeting" give the indeces for the output of the greetings?

print('===========================')

for number in range(10, 20):
    print(number)

print('=================')
# find the even numbers from the range of 50 to 71

for number in range(50, 71, 2):
    print(number)

print('===========================')

# create a python program that prints odd numbers from 100 to 150

for number in range(101, 150, 2):
    print(number)

print('===========================')

# create a program that prints the miltiples of 3 starting from 201 to 150

for number in range(201, 149, -3):
    print(number)

print('===========================')

# create a python program that prints the leap years in between 2000 and 2024

for year in range(2000, 2025, 4):
    if year%400 == 0:
        print(year) 