lista = []
count = 0
while True:
    heltal = input("Skriv ett heltal eller (q) när du är klar: ")
    if heltal == "q".lower():
        break
    else:
        lista.append(int(heltal))
for c in range(0, len(lista)):
    if lista[c] < 0:
        count +=1

print(count)