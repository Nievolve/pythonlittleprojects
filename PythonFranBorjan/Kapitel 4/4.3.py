n = int(input("n?: "))

a = 1
b = 1
c = 0
summa = 0
stopp = 1
while stopp <= n:
    c = a / b
    summa += c
    b += 1
    stopp +=1

print (summa)