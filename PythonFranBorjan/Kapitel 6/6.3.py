#Skriv ett progra som skapar en lista med 100 slumpmässiga heltal i intervallen 1-1000.
#Programmet ska sedan skriva it det minsta och det största av talen och skriva ut slumptalens medelvärde

import random
lista_a = []
k = -1
total = 0
for x in range(0, 100,1):
    lista_a.append(random.randint(1,1000))
for e in lista_a:
    total = total + e


a = total //1000
print("Medelvärdet på listan är", a)

print(min(lista_a))
print(max(lista_a))

