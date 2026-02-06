# Below is a grading system based on what a student will haev gotten
marks = int(input("Enter Student Marks: "))
# print("The entered marks are ", marks)

if marks > 0 and marks < 30:
    print("Below Average")
elif marks >= 30 and marks < 40:
    print("Average")
elif marks >= 40 and marks < 70:
    print("Above Average")
elif marks >= 70 and marks <=100:
    print("Excellent")
else:
    print("Invalid Input")