currentDayNumber = eval(input("Enter today's day: "))
numOfDaysElapsed = eval(input("Enter the number of days elapsed since today: "))
futureDayNumber = (currentDayNumber + numOfDaysElapsed) % 7
currentDayName = ""
futureDayName = ""

if currentDayNumber == 0:
    currentDayName = "Sunday"
elif currentDayNumber == 1:
    currentDayName = "Monday"
elif currentDayNumber == 2:
    currentDayName = "Tuesday"
elif currentDayNumber == 3:
    currentDayName = "Wednesday"
elif currentDayNumber == 4:
    currentDayName = "Thursday"
elif currentDayNumber == 5:
    currentDayName = "Friday"
elif currentDayNumber == 6:
    currentDayName = "Saturday"

if futureDayNumber == 0:
    futureDayName = "Sunday"
elif futureDayNumber == 1:
    futureDayName = "Monday"
elif futureDayNumber == 2:
    futureDayName = "Tuesday"
elif futureDayNumber == 3:
    futureDayName = "Wednesday"
elif futureDayNumber == 4:
    futureDayName = "Thursday"
elif futureDayNumber == 5:
    futureDayName = "Friday"
elif futureDayNumber == 6:
    futureDayName = "Saturday"

print(f"Today is {currentDayName} and the future day is {futureDayName}")

