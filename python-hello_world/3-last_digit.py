import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    print("Last digit of", number, "is", -last_digit, end="")
else:
    print("Last digit of", number, "is", last_digit, end="")

if last_digit > 5 and number > 0:
    print(" and is greater than 5",end="\n")
elif last_digit == 0:
    print(" and is 0", end="\n")
else:
    print(" and is less than 6 and not 0", end="\n")