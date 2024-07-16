import random
digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0, 9)
sum = digit1 + digit2 + digit3
solution = eval(input(f"{digit1} + {digit2} + {digit3} = "))
if solution == sum:
    print("That's correct!")
else:
    print("Wrong answer!")