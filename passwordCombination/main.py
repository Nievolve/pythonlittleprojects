
matrixx = []
matrixy = []
matrixxy = []
listOfstring = ["agesson","ageskar","admin","DBEED5ACFB"]
for user in range (0,len(listOfstring)):
    targetString = listOfstring[user]
    for password in listOfstring:
        matrixx.append(targetString)
        matrixy.append(password)

for index in range (0,len(matrixx)):
    matrixxy.append([matrixx[index]],[matrixy[index]])


for row in matrixxy:
    for element in row:
        print(element)

