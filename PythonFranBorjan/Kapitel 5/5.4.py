a = input(":  ")
#Räknare
i = 0

for k in range(len(a), 0,-1):
    if k == " " or k == "\t":
        break
    i +=1

print("Sista mellanslaget i texten ligger på plats ",end="")
print(i)

