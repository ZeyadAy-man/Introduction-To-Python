import math
investmentAmount = eval(input("Enter investement amount: "))
annualInterestRate = eval(input("Enter annual interest rate: "))
numberOfYears = eval(input("Enter number of years: "))
futureInvestmentValue = investmentAmount * (math.pow((1 +  annualInterestRate / 12 / 100), numberOfYears * 12))
print("Accumulated value is ", futureInvestmentValue)