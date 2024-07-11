minutes = eval(input("Enter the number of minutes: "))
days = minutes // (60 * 24)
print(minutes, "minutes is approximately ", (days // 365), " years and ", (days % 365), "days")