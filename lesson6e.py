# On the try and except block, you run some codes/ statements and if successful, the try block will be executed otherwise the except block will be executed when there is an anticipated error.

try:
    number = 100
    answer = number / 0
    print("The answer is: ", answer)
except Exception as e:
    print("There is an error: ", e)