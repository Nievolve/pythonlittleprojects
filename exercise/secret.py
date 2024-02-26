import random

answer = random.randint(1,100)


svar = 0
try1 = 0

while svar != answer:
    print(answer)
    print("Du har försökt " + str(try1) + " gånger")
    svar = int(input("Input: "))
    try1 += 1
    if svar > answer:
        print("Lägre")
    elif svar < answer:
        print("Högre")
    else:
        pass
print("DU HAR GISSAT RÄTT! Det tog " + str(try1) + " försök")





while True:
    user_guess = input("Enter Number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please, enter a number")
        continue
    if user_guess == answer:
        break
