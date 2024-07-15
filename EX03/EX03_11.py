number = eval(input("Enter an integer: "))
digit1 = number % 10
number = number // 10
digit2 = number % 10
number = number // 10
digit3 = number % 10
number = number // 10
digit4 = number % 10
number = number // 10
print(f"The reversed number is {digit1}{digit2}{digit3}{digit4})")
