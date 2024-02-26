heltal = []
while True:
    s = input("Skriv in heltal. Avsluta på med Q: ")
    if s.lower() == "q":
        break
    elif s not in heltal:
        heltal.append(s)
    else:
        pass
print(heltal)



