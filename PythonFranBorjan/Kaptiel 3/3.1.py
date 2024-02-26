
##Input två variablar
minuter = int(input("Antal minuter: "))
kostnad = int(input("Kostnad per minut: "))
##  #

month = minuter * kostnad
total = month
if month >= 300:
    total = month * 0.9

print(f"{total:.0f}")
