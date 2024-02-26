s = 129
talet = int(s)
primtal = []
if s >= 3:
    primtal.append(1)
    primtal.append(2)
    primtal.append(3)
else:
    pass
for k in range(1, talet):
    if k == 1 or k == 2 or k ==3:
        pass
    else:
        if k % 2 == 0 or k % 3 == 0:
            pass
        else:
            primtal.append(k)

print(primtal)