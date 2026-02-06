# Boolean - This is a data type that evaluates either True or False
# We so not use quotes for True and False

israining = False
print(israining)
print(type(israining))

paidloan = True
print(paidloan)
print(type(paidloan))

# Comparison Operators: They are used to compare 2 or more statements and they usually return a boolean asnswer

number1 = 2
number2 = 5

print("Is number1 greater than number2?", number1 > number2)
print("Is number1 less than number2?", number1 < number2)
print("Is number1 greater than or equal to number2?", number1 >= number2)
print("Is number1 less than or equal to number2?", number1 <= number2)
print("Is number1 equal to number2?", number1 == number2)
print("Is number1 not equal to number2?", number1 != number2)

# Logical Operators

# Operator and
#   and returns True if all conditions are fulfilled (both statements are true) and False if any or all statements are false

print("For the two statements:",
      (3>1) and (7>6))

# Operator or
# or returns True of any of the statements, conditions is true and False if all statements are false

print("For the two statements:", (3>1) or (7<6))
print("For the two statements:", (3<1) or (7<6))
print("For the two statements:", (3>1) or (7<6) or (10>5))

# Operator not
# It is used to negate statements/ conditions
print("For the two statements:", not(90>70))