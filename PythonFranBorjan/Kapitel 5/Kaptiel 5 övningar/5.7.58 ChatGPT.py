from datetime import datetime

# Läs in två tider
time1 = input("Ange den första tiden (HH:MM): ")
time2 = input("Ange den andra tiden (HH:MM): ")

# Konvertera tiderna till datetime-objekt
time1 = datetime.strptime(time1, "%H:%M")
time2 = datetime.strptime(time2, "%H:%M")


# Räkna ut skillnaden i minuter
diff = int((time2 - time1).total_seconds() / 60)

# Om diff är negativ, lägg till 24*60 minuter (ett helt dygn) eftersom vi antar att tiden har gått till nästa dag
if diff < 0:
    diff += 24 * 60

# Skriv ut skillnaden
print(f"Skillnaden mellan de två tiderna är {diff} minuter.")
