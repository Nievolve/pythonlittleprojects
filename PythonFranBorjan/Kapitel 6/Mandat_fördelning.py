antal_mandat = int(input("Antal mandat: "))
spärr = int(input("Spärr för småpartier: "))
s = input("Antal röster : ")
röster = [int(x) for x in s.split()]
totalt = sum(röster)
mandat = [0] * len(röster)
jftal = []
for i in range(0 , len(röster)):
    if röster[i] /totalt > spärr:
        röster[i] = 0
    print(röster[i])
    jftal.append(röster[i])
print(jftal)
for i in range(0 , antal_mandat):
    m = max(jftal)
    p = jftal.index(m)
    mandat[p] += 1
    jftal[p] = röster[p] / (2*mandat[p]+1)

print("Mandatfördelning")
print(mandat)