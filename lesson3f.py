# Create a python program that is able to determine whether a number entered is an odd number or an even number
# number = int(input("Enter Number"))
# if number%2 == 0:
#     print("The number is even")
# else:
#     print("Number is odd")

# Create a python program that can be able to determine whether a person can donate based on the weight and age ofa teh person. If the weight is above 50kg and the age is above 18, the person can donatem else they cannot
age = int(input("Enter age "))
weight = float(input("Enter weight "))
if weight > 50 and age > 18:
    print("You can donate blood")
else:
    print("You cannot donate blood")