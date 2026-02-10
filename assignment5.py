# Question 1: Function without Parameters

def area():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    prodcut = length * width
    print("The area of the rectangle is: ", prodcut, "squared units")

area()

print("===============================")
# Question 2: Function with Parameters

def numbers(number1, number2):
    sum = number1 + number2
    difference = number2 - number1
    product = number1 * number2
    quotient = number2 / number1
    print(f"The sum of the two numbers is {sum}")
    print(f"The difference between the two numbers is {difference}")
    print(f"The prodcut of the two numbers is {product}")
    print(f"The quotient of the two numbers is {quotient}")

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

numbers(number1, number2)

print("===============================")

# Question 3: Control Statement

number = float(input("Please enter the number: "))

if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
else:
    print("The number entered is zero")


print("===============================")
# Question 4: Loop with arithmetic (for loop)

n = int(input("Enter a number (n): "))
total_sum = 0

for number in range(1, n + 1):
    total_sum = total_sum + number

print(f"The sum of numbers from 1 to {n} is: {total_sum}")

print("===============================")

# Question 5: while loop

def square_numbers():
    n = int(input("Enter a number: "))
    current = 1
    
    while current <= n:
        square = current ** 2
        print(f"The square of {current} is {square}")
        current += 1

square_numbers()

