subtotal = eval(input("Enter the subtotal: "))
gratuityRate = eval(input("Enter the gratuity rate: "))
print("The gratuity is", (gratuityRate / 100 * subtotal), "and the total is", (gratuityRate / 100 * subtotal + subtotal))