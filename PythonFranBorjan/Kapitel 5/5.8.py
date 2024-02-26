a = "Hej på dig denna mening innehåller 8 antal mellanslag"
print(a)

#Splitar upp strängen i en lista
b = a.split()
j = 0
c = len(b)
#Cyclar igenom listan indexvis
for k in range(0, c,1):
    k = b[j]
    j +=1
    print(k, end="")
print("")
