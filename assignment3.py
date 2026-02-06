# NHIF monthly contribution program
salary = int(input("Enter Salary: "))

if salary > 0 and salary < 5999:
    print("Your monthly contribution is: Ksh 150.00")
elif salary >= 6000 and salary < 8000:
    print("Your monthly contribution is: KSh 300.00")
elif salary >= 8000 and salary < 12000:
    print("Your monthly contribution is: Ksh 400.00")
elif salary >= 12000 and salary < 15000:
    print("Your monthly contribution is: Ksh 500.00")
elif salary >= 15000 and salary < 20000:
    print("Your monthly contribution is: Ksh 600.00")
elif salary >= 20000 and salary < 25000:
    print("Your monthly contribution is: KSh 750.00")
elif salary >= 25000 and salary < 30000:
    print("Your monthly contribution is: Ksh 850.00")
elif salary >= 30000 and salary < 50000:
    print("Your monthly contribution is: Ksh 1,000.00")
elif salary >= 50000 and salary < 100000:
    print("Your monhtly contribution is: Ksh 1,500.00")
elif salary >= 100000:
    print("Your monthly contribution is: Ksh 2,000.00")
else:
    print("Invalid Entry")