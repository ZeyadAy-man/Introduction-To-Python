initialVelocity = eval(input("Enter initial velocity: "))
finalVelocity = eval(input("Enter final velocity: "))
durationTime = eval(input("Enter duration time: "))
averageAcceleration = (finalVelocity - initialVelocity) / (durationTime)
print("The average acceleration is ", averageAcceleration)