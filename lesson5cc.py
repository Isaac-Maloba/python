# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.

def simple_interest(p, r, t):
    interest = (p*r*t)/100
    print(f"The simple interest is {interest}")

simple_interest(45000, 7, 8)

for stuff in range(1):
    simple_interest(60000, 12, 11)
    simple_interest(13000, 32, 14)