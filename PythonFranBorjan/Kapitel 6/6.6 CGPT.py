user_range = int(input("Hur hög tabell?:  "))
table_1 = []
for m in range(1, user_range+1):
    sublist = []  # skapa en ny lista för varje 'm'
    for c in range(1, user_range+1):
        sublist.append(c*m)  # lägg till produkten till den nya listan
    table_1.append(sublist)  # lägg till den nya listan till huvudlistan

for row in table_1:
    print(row)
