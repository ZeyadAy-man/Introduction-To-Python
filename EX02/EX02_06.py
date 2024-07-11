digit = eval(input("Enter a number between 0 and 1000: "))
digit1 = digit % 10
digit = digit // 10
digit2 = digit % 10
digit = digit // 10
digit3 = digit % 10
print("The sum of the digits is ", (digit1 + digit2 + digit3))