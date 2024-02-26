import datetime
dt = datetime.datetime.now()
prsnr = "9007262974"

dtext = str(dt)

print(dtext)

birthday = dtext [5:7] + dtext [8:10]
check_birthday = prsnr[2:6]
print(birthday)
print(check_birthday)

if check_birthday == birthday:
    print("Grattis")
else:
    print("Vanlig dag")