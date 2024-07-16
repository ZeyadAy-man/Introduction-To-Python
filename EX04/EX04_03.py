a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))
d = eval(input("Enter d: "))
e = eval(input("Enter e: "))
f = eval(input("Enter f: "))

divisor = a * d - b * c
if divisor == 0:
    print("The equation has no solution.")
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print(f"x is {x} and y is {y}")
