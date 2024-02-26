#Skriv ett program som läser in en lista med heltal. Programmet ska sedan ta bort alla element från listan som är lika med noll.
#Tips: Tänk på att det kan finnas fler sådana element
lista_a =input("Skriv lista: ")
lista_b = lista_a.split()
lista_b = [int(x) for x in lista_b]
lista_b.sort()
antal = lista_b.count(0)
del lista_b[0:antal:1]
print(lista_b)
