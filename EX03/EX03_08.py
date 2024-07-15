money = eval(input("Enter the money: "))
cents = money % 100
dollars = money // 100
print(f"you have {dollars} dollars and {cents} cents")