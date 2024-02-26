#Skriv ett program som jämnför en lista och tuple.
#Listan och tuplern ska läsas in till programmet innan jämnförelsen görs.
#Programmet ska ange om listan och tuplern är lika långa eller inte.
#Ditt program ska uppfatta dem som lika om det är lika långa och motsvarande element är lika.
tupler = (1,2,3)
lista = [2,1,3]
if list(tupler) ==lista:
    print("Lika")
else:
    print("Olika")