point = int(input("Antal poäng"))
betyg = "A"
if point < 25:
    betyg = "F"
elif point <= 26 and point <= 29:
    betyg = "E"
elif point <= 30 and point <= 34:
    betyg = "D"
elif point <= 35 and point <= 39:
    betyg = "C"
elif point <= 40 and point <= 44:
    betyg = "B"
elif point <= 45 and point <= 50:
    betyg = "A"
print(point)
print(betyg)