monthlySavingAmount = eval(input("Enter the monthly saving amount: "))
MULTIPLIEDCONSTANT = (1 + 0.00417)
afterTheFirstMonth = monthlySavingAmount * MULTIPLIEDCONSTANT
afterTheSecondMonth = (afterTheFirstMonth + monthlySavingAmount) * MULTIPLIEDCONSTANT
afterTheThirdMonth = (afterTheSecondMonth + monthlySavingAmount) * MULTIPLIEDCONSTANT
afterTheFourthMonth = (afterTheThirdMonth + monthlySavingAmount) * MULTIPLIEDCONSTANT
afterTheFifthMonth = (afterTheFourthMonth + monthlySavingAmount) * MULTIPLIEDCONSTANT
afterTheSixthMonth = (afterTheFifthMonth + monthlySavingAmount) * MULTIPLIEDCONSTANT
print("After the sixth month, the account value is ", afterTheSixthMonth)