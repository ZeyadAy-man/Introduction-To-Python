integer = eval(input("Enter a 4-digit integer: "))
digit1 = integer % 10
integer = integer // 10
digit2 = integer % 10
integer = integer // 10
digit3 = integer % 10
integer = integer // 10
digit4 = integer % 10
integer = integer // 10
print(digit4)
print(digit3)
print(digit2)
print(digit1)