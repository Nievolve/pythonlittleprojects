#Utskriften från programmet som skapar en multiplikationstabell blir inte så snygg.
#Dessutom vill man kanske inte alltid ha en tabell för tal upp till 10.
#Skriv en ny version av programmet där man låter den som kör programmet bestämma vilket ska vara den övre gränsen i tabellen.
#Ändra också utskriften så att varje rad i tabellen hamnar på en egen rad i utskriften.
user_range = int(input("Hur hög tabell?:  "))
table_1 =[]
for m in range(1, user_range+1):
    for c in range(1, user_range+1):
        table_1.append(c*m)



print(table_1[80])
