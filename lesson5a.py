# PYTHON FUNCTIONS
# They are a block of code, statements that perform a given task/ action. They can be re-used throughout the program to perform different tasks
# Functions are defined using the "def" key word (define)
# We have 2 main types of functions i.e
    # In-built functions -> They come pre-installed with th interpretor e.g print (), pop (), range(), append ()
    # User-defined functions -> They are created by a programmer to solve a given task that sutes the entire    program
# To define a function, you need to give it a name followed by parenthesis.
# For the function body, it is usually indented and to invoke a function we use the function name

def greeting():
    print("Hello, how are you?")

# belw we call the function by use of its name
greeting

print('=================================')
# addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)

# calling the function for the operation above
addition()

print('=================================')
# create a function that is able to multiply 3 values

def multiplication():
    num4 = 15
    num5 = 20
    num6 = 25
    product = num4 * num5 * num6
    print("The product of the three numbers is: ", product)

# Read on local variables
multiplication()

print('=================================')

# Blow is a divisin function
def divide():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    quotient = number1 / number2
    print("The quotient of the two numbers is: ", quotient)
    print('---------')

for function in range(3):
    divide()



