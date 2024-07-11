finalAccountValue = eval(input("Enter the final account value : "))
annualInterestRate = eval(input("Enter the annual interest rate in percent : "))
numberOfYears = eval(input("Enter the number of years : "))

monthlyInterestRate = (annualInterestRate / 12) / 100
numberOfMonths = 12 * numberOfYears

initial_deposit_value = finalAccountValue / ((1 + monthlyInterestRate) ** numberOfMonths)
print("Initial deposit value", initial_deposit_value)