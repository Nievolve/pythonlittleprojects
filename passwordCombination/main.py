matrixx = []
matrixy = []
matrixxy = []
listOfstring = ["agesson", "ageskar", "admin", "DBEED5ACFB", "Hej", "påDig", "din luring"]

for user in range(len(listOfstring)):
    targetString = listOfstring[user]
    for password in listOfstring:
        matrixx.append(targetString)
        matrixy.append(password)

for index in range(len(matrixx)):
    matrixxy.append([matrixx[index], matrixy[index]])

for row in matrixxy:
    print(row)
    
