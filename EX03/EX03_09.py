employeeName = input("Enter employee's name: ")
numberOfWorkedHours = eval(input("Enter number of hours worked in a week: "))
payRate = eval(input("Enter hourly pay rate: "))
federalTaxWithHoldingRate = eval(input("Enter federal tax withholding rate: "))
stateTaxWithHoldingRate = eval(input("Enter state tax withholding rate: "))
grossPay = payRate * numberOfWorkedHours
federalTax = federalTaxWithHoldingRate * grossPay
stateTax = stateTaxWithHoldingRate * grossPay
totalTax = stateTax + federalTax
print(f"Hours Work: {numberOfWorkedHours}")
print(f"Pay Rate: {payRate}")
print(f"Gross Pay: {grossPay}")
print("Deductions:")
print(f"    Federal Withholding ({federalTaxWithHoldingRate * 100}%): ${federalTax}")
print(f"    State Withholding ({stateTaxWithHoldingRate * 100}%): ${stateTax:.2f}")
print(f"    Total Deductions: ${totalTax:.2f}")
print(f"New Pay: ${grossPay - totalTax:.2f}")