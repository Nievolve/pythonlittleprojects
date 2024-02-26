dmg_1 = 1
dmg_2 = 1
round = 0
add = 1
while dmg_1 < 99 and dmg_2 < 99:
    dmg_1 += 1
    round +=1
    dmg_2 +=add
    add += round / 3
    print(dmg_1)
    print(dmg_2)

print (round)
print(dmg_1)
print(dmg_2)