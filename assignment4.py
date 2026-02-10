# Looping through the list of colors assignment
colors = ["Blue", "Green", "Red", "Pink", "Black"]
for color in colors:
    print(color)

print('================================')

# for loop for leap years from 2000 to 2024
for year in range(2000, 2025):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)

print('=================================')


# while loop that prints numbers from 20 to 1
num = 20

while num >= 1:
    print(num)
    num -= 1
