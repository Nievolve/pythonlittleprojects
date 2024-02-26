import random
computor_wins = 0
user_wins = 0


while True:
    while True:
        print("Sten, sax, påse?")
        user_choice = input(": ")
        if user_choice.lower() =="avsluta":
            quit()
        if user_choice.isalpha():
            if user_choice.lower() in ["sten" , "sax" , "påse"]:
                break
            else:
                print("Error 01")
                continue
        else:
            print("Error 02")
            continue

    computor_choice = random.randint(1,3)
        # 1. Sten 2. Sax 3. Påse
    if user_choice.lower() == "sten" and computor_choice == 2:
        print("Du har valt " + str(user_choice.lower()) +" och datorn har valt sax")
        print("Du vinner!!")
        user_wins += 1
    elif user_choice.lower() == "sten" and computor_choice == 3:
        print("Du har valt " + str(user_choice.lower()) + " och datorn har valt påse")
        print("Datorn vinner!!")
        computor_wins += 1
    elif user_choice.lower() == "sax" and computor_choice == 3:
        print("Du har valt " + str(user_choice.lower()) + " och datorn har valt påse")
        print("Du vinner!!")
        user_wins += 1
    elif user_choice.lower() == "sax" and computor_choice == 1:
        print("Du har valt " + str(user_choice.lower()) + " och datorn har valt påse")
        print("Datorn vinner!!")
        computor_wins += 1
    elif user_choice.lower() == "påse" and computor_choice == 1:
        print("Du har valt " + str(user_choice.lower()) + " och datorn har valt sten")
        print("Du vinner!!")
        user_wins += 1
    elif user_choice.lower() == "påse" and computor_choice == 2:
        print("Du har valt " + str(user_choice.lower()) + " och datorn har valt påse")
        print("Datorn vinner!!")
        computor_wins += 1
    else:
        print("Du har valt " + str(user_choice) + " och datorn har valt " + str(user_choice))
        print("Det är oavgjort, spela igen")

    print(str(user_wins) + " / " + str(computor_wins))