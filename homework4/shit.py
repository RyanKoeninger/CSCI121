mins = input("Minutes after midnight? ")
hours = int(mins) // 60
minutes = int(mins) % 60

if int(hours) == 0:
    hrStr = str("00")
elif int(hours) < 10:
    hrStr = str("0") + str(hours)
elif int(hours) % 24 == 0:
    hrStr = str("12")
else:
    hrStr = str(hours)
if minutes == 0:
    minStr = "00"
elif minutes < 10:
    minStr = "0" + str(minutes)
else: 
    minStr = str(minutes)

print("The time is " + str(hrStr) + ":" + str(minStr) + ".")