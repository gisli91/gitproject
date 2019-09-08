import math

seconds_given = int(input("Please give a specific second of the day: "))

hours = 0
minutes = 0 
seconds = 0

if seconds_given > 0 and seconds_given <= 86400:
    hours = int(seconds_given / 60 / 60)
    minutes = int((seconds_given / 60) - hours * 60 )
    seconds = int(seconds_given - (hours * 60**2)-(minutes * 60))
    print(hours , minutes, seconds)










else:
    print("Not a valid second of the day!")