test = "ni talar bra latin"
test_1 = test.replace(" ", "")
list = []
for k in test_1:
    list.append(k)
print(list)
index = len(list)
front_number, back_number = index//2, index//2
print(front_number,back_number)
k1 = 0
for k in (list, len(front_number), 1):
    print(k)


