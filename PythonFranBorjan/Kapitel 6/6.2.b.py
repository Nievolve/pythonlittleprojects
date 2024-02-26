i = input("Tal: ")
lista = i.split()                       #Splittar strängen till en lista
lista_b = [ int(x) for x in lista] #Gör om från string till integer
lista_c = [x for x in lista_b if x < 0] #Gör en lista som endast innehåller de element från lista_b
print(len(lista_c)) #Skriver ut längden på lista_c som nu bara inehåller interger element som är större än 0