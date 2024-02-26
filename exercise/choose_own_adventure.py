name_char = input("What is your name?: ")
print("Welcome to the game, ", name_char)

print("You are at a dirt road crossing, walk left or right? ")
choice_01 = input(": ").lower()

if choice_01 == "left":
    print("You walk left")
    print("You come to a bridge but it's broken, jump over it or swim?")
    choice_02 = input(": ").lower()

    if choice_02 == "jump":
        print("You jump, but fall onto some jagged rocks. You lose")
    elif choice_02 == "swim":
        print("You swim over the river and come to the other side.")
        print("You see a horse and a car, which do you choose?")
        choice_03 = input(": ").lower()

        if choice_03 == "horse":
            print("You sit on the horse but the horse doesn't like you, it kicks you. You lose!")
        elif choice_03 == "car":
            print("You sit in the car and start it, you drive and come to a crossing. Left or right?")
            choice_04 = input(": ").lower()

            if choice_04 == "left":
                print("The road ends with a cliff, and the car's brakes don't work... You lose!")
            elif choice_04 == "right":
                print("You arrive at a cabin, the car's gas tank is empty. Do you enter the cabin or continue walking?")
                choice_05 = input(": ").lower()

                if choice_05 == "enter":
                    print("You enter the cabin, inside waits a man with an ax. You lose!")
                elif choice_05 == "walking":
                    print("You walk down the road and arrive at your house. You win")
                    print("Winner winner chicken dinner")
                else:
                    print("You typed", choice_05, ". You lose")
            else:
                print("You typed", choice_04, ". You lose")
        else:
            print("You typed", choice_03, ". You lose")
    else:
        print("You typed", choice_02, ". You lose!")
elif choice_01 == "right":
    print("You walk right")
else:
    print("You typed", choice_01, ". You lose")



print(" Take  TWO")
name_char = input("What is your name?: ")

print("Welcome to the game, " , name_char)

print("You are at a dirt road crossing, walk left or right? ")
choice_01 = input(": ").lower()
if choice_01 == "left":
    print("You walk left")
    print("You come to a bridge but it's broken, jump over it or swim?")
    choice_01 = input(": ").lower()
    if choice_01 == "jump":
        print("You jump, but falls down on to some jagged rocks. You lose")

    elif choice_01 == "swim":
        print("You swim over the river and come to the other side.")
        print("You see a horse and a car, which do you choose?")
        choice_01 = input(": ").lower()
        if choice_01 == "horse":
            print("You sit on the horse but the horse does not like you, it kicks you. You lose!")
        elif choice_01 == "car":
            print("You sit in the car and start it, you drive and comes to a crossing. Left or right?")
            choice_01 = input(": ").lower()
            if choice_01 == "left":
                print("The road ends with a cliff, and the brakes of your car does not work... You lose!")

            elif choice_01 == "right":
                print("You arrive at a cabin, the cars gastank is empty. Do you enter the cabin or continue walking?")
                choice_01 = input(": ").lower()
                if choice_01 == "left":
                    print("The road ends with a cliff, and the brakes of your car does not work... You lose!")

                elif choice_01 == "right":
                    print("You arrive at a cabin, the cars gastank is empty. Do you enter the cabin or continue walking?")
                    choice_01 = input(": ").lower()
                    if choice_01 == "enter":
                        print("You enter the cabin, inside waits a man with an ax. You lose!")
                    elif choice_01 == "walking":
                        print("You walk down the road and arrive at your house. You win")
                        print("Winner winner chicken dinner")
                    else:
                        print("You typed", choice_01, ". You lose")
                else:
                    print("You typed", choice_01, ". You lose")
            else:
                print("You typed", choice_01, ". You lose")
        else:
            print("You typed", choice_01, ". You lose")

    else:
        print("You typed" , choice_01 , ". You lose!")
elif choice_01 == "right":
    print("You walk right")
else:
    print("You typed" , choice_01 , ". You lose")

