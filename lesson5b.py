# Functions with Parameters
# Parameters are values that get passed as arguments given to a function inside of the parenthesis

def greeting(name):
    print(f"{name} How are you? Hope everything is fine.")

greeting("Maloba")
greeting("Isaac")
greeting("Wanyama")

print("=========================")

def message(name):
    print(f"Hello {name}, we shall be having a meeting tomorrow at the usual meeting time; please avail yourself")

message("Natalie")
message("Karay")

print("===========================")
# Create a function that accepts a parameter to add 2 numbers


def additon(x, y):
    sum = x + y
    print(f"The sum of the numbers is {sum}")

additon(25, 70)