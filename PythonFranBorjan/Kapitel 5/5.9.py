a = "ni talar bra latin"

print(a)

#Splitar upp strängen i en lista
b = a.split()
j = 0
c = len(b)
print(b)

#Cyclar igenom listan indexvis
for k in range(0, c,1):
    k = b[j]
    j +=1
    print(k, end="")

print("")
e = len(b)
d = b[e-4]+""+b[e-3]+""+b[e-2]+""+b[e-1]+""
print(d)



