import math
a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))

discriminant = b * b - 4 * a * c
if discriminant > 0:
    r1 = (- b + math.sqrt(discriminant)) / 2 * a
    r2 = (- b - math.sqrt(discriminant)) / 2 * a
    print(f"The roots are {r1:.6f} and {r2:.6f}")
elif discriminant < 0:
    print("The equation has no real roots.")
else:
    r = - b / (2 * a)
    print(f"The root is {r}")
