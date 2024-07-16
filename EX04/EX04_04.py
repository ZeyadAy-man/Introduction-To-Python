import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

solution = eval(input(f"{num1} + {num2} = "))

if solution == (num1 + num2):
    print("That's correct!")
else:
    print("Wrong answer!")