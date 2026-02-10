# A python for loop can also be used to iterate through a list, a tuple, a string or even a dictionary

name = "Bernard"

for letter in name:
    if letter == "n":
        print("The letter is n")
    else:
        print(letter)

print('===========================')

# below is a list of counties
counties = ["Nairobi", "Mombasa", "Kisumu", "Uasin Gishu", "Kajiado", "Machakos", "Meru", "Bungoma"]
print(counties)

for county in counties:
    print(county)

print('===========================')
# how do i search for specific county from the list and print "county found" using the user's input using search and for

if "Kajiado" in counties:
    print("Kajiado is in the list of counties")
else:
    print("Kajiado is not in the list of counties")

print('===========================')

for county in counties: # how do I print a single output here
    if county == "Kajiado":
        print("The county is part of the list")
        break # what is the use of this break
    else:
        print("The county is not part of the list")

print('===========================')

# the for loop can also be used to iterate through a dictionary
# wtf does using dot do? e.g players.values

player = {
    "name": "Mbappe",
    "age": 25,
    "teams": ["PSG", "Monaco", "France"],
    "Nationality": "French"
}


for key in player:
    print(key)

print('===========================')

for value in player:
    print(player[value]) # wtf does values do????
# i don't even know what a key is, or a string
# printing values from the dictionary using the for loop

print('===========================')

# loop through the teams has played for
# hwo do i loop through a list in a dictionary?
# looping thru shii; i simply not getting shii

print('===========================')

for teams in player["teams"]:
    print(teams)



print('===========================')

word = "maloba"
for character in word:
    print(character)

print('===========================')

for character in word:
    if character == "b":
        print("The character is b")
    else:
        print(character)

name = "Bernard"
count = 0

for letter in name:
    if letter == "r":
        count = count + 1

print(f"The letter 'r' appears {count} times")
# Output: The letter 'r' appears 2 times


word = "Python"

for letter in word:
    if letter in ["a", "e", "i", "o", "u"]:
        print(letter, "is a vowel")
    else:
        print(letter, "is a consonant")


name = "wanyama"
uppercase_name = ""

for letter in name:
    uppercase_name = uppercase_name + letter.upper()

print(uppercase_name)

"""
Start with empty string: ""
Add "B" → "B"
Add "E" → "BE"
Add "R" → "BER"
Add "N" → "BERN"
Add "A" → "BERNA"
Add "R" → "BERNAR"
Add "D" → "BERNARD"
"""

word = "hello"
result = ""

for letter in word:
    if letter == "l":
        result = result + "L"  # Make 'l' uppercase
    else:
        result = result + letter

print(result)
# Output: heLLo


## **Common Mistakes and Clarifications**

### **Mistake 1: Thinking the loop runs once**
# ❌ **Wrong:** "The loop checks if any letter is 'n'"
# ✅ **Correct:** "The loop checks EACH letter one by one, 7 separate times"

### **Mistake 2: Thinking letter stores all characters**
# ❌ **Wrong:** `letter = "Bernard"`
# ✅ **Correct:** `letter = "B"` (first time), then `"e"` (second time), etc.

### **Mistake 3: Forgetting the loop continues after finding "n"**
# The loop doesn't stop after finding "n" - it keeps going through the remaining letters (a, r, d).


## **Visualizing the Loop Flow**

# Start Loop

# letter = "B"  →  Check if "B" == "n"  →  NO  →  Print "B"

# letter = "e"  →  Check if "e" == "n"  →  NO  →  Print "e"

# letter = "r"  →  Check if "r" == "n"  →  NO  →  Print "r"

# letter = "n"  →  Check if "n" == "n"  →  YES  →  Print "The letter is n"

# letter = "a"  →  Check if "a" == "n"  →  NO  →  Print "a"

# letter = "r"  →  Check if "r" == "n"  →  NO  →  Print "r"

# letter = "d"  →  Check if "d" == "n"  →  NO  →  Print "d"

# End Loop (no more letters)

fruits = ["apple", "banana", "apple", "orange", "apple"]
count = 0

for fruit in fruits:
    if fruit == "apple":
        count = count + 1

print(f"Found {count} apples")
# Output: Found 3 apples

counties = ["Nairobi", "Mombasa", "Kisumu", "Kajiado"]
position = 0

for county in counties:
    if county == "Kajiado":
        print(f"Kajiado is at position {position}")
        break
    position = position + 1

# Output: Kajiado is at position 3

numbers = [1, 2, 3, 4, 5]
doubled = []

for number in numbers:
    doubled.append(number * 2)

print(doubled)
# Output: [2, 4, 6, 8, 10]

