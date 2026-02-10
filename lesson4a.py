# Nested If Statements
# A nested if statement is an if statement that is contained antoher if statement

age = 10
weight = 40

if age > 15:
    if weight > 50:
        print("You can donate blood")
    else:
        print("You cannot donate blood becaus of your weight")
else:
    print("You cannot donate blood because of your age")