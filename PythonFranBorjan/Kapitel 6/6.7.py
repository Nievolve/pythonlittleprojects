print("Skriv in en matrik rad för rad.")

m = []
while True:
    s = input("? ")
    if s.lower() == "q":
        break

    ls = s.split(",")
    rad = [float(e) for e in ls]
    m.append(rad)



print(m)