# Skapa en tom lista för att lagra personuppgifter
personer = []

# Läs in personuppgifter tills användaren väljer att avsluta
while True:
    namn = input("Ange personens namn (eller 'avsluta' för att avsluta): ")
    if namn.lower() == "avsluta":
        break

    kön = input("Ange personens kön (man/kvinna): ")
    ålder = int(input("Ange personens ålder: "))

    # Skapa en dictionary för att lagra personens uppgifter
    person = {
        "namn": namn,
        "kön": kön,
        "ålder": ålder
    }

    # Lägg till personen i listan
    personer.append(person)

# Räkna antalet kvinnor och män och summera åldrarna för respektive kön
antal_kvinnor = 0
antal_män = 0
ålder_kvinnor = 0
ålder_män = 0

for person in personer:
    if person["kön"].lower() == "kvinna":
        antal_kvinnor += 1
        ålder_kvinnor += person["ålder"]
    elif person["kön"].lower() == "man":
        antal_män += 1
        ålder_män += person["ålder"]

# Beräkna genomsnittsåldern för kvinnor och män (om det finns minst en person av varje kön)
if antal_kvinnor > 0:
    genomsnitt_ålder_kvinnor = ålder_kvinnor / antal_kvinnor
else:
    genomsnitt_ålder_kvinnor = 0

if antal_män > 0:
    genomsnitt_ålder_män = ålder_män / antal_män
else:
    genomsnitt_ålder_män = 0

# Skriv ut resultaten
print(f"Antal kvinnor: {antal_kvinnor}")
print(f"Antal män: {antal_män}")
print(f"Genomsnittlig ålder för kvinnor: {genomsnitt_ålder_kvinnor}")
print(f"Genomsnittlig ålder för män: {genomsnitt_ålder_män}")
