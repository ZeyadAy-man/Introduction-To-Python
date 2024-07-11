import time
timeZoneOffset = eval(input("Enter the time zone offset to GMT: "))
currentTime = time.time()
totalSeconds = int(currentTime)
currentSeconds = int(totalSeconds % 60)
totalMinutes = totalSeconds // 60
currentMinutes = int(totalMinutes % 60)
totalHours = currentMinutes // 60
currentHours = int(currentMinutes % 24) + -1 * (timeZoneOffset) - 1
print("The current time is ", currentHours, ":", currentMinutes, ":", currentSeconds)