        #Introducerar random modulen
import random
        ##

        #Funktion som genererar och definerar datorns gissning till en variabel

def game_time(computor_choice, user_guess):
    if computor_choice == 1 and user_guess == "påse":
        print("Användaren vinner")
    elif computor_choice == 3 and user_guess == "sten":
        print("Datorn vinner")
    elif computor_choice == 2 and user_guess == "påse":
        print("Datorn vinner")
    elif computor_choice == 3 and user_guess == "sax":
        print("Användaren vinner")
    elif computor_choice == 1 and user_guess == "sax":
        print("Datorn vinner")
    elif computor_choice == 2 and user_guess == "sten":
        print("Användaren vinner")
    else:
        tie_breaker = True
        print("Det är oavgjort.")
        return tie_breaker


while True:

    user_guess = input("Sten, sax or påse?: ")
    if user_guess.isalpha():
        if user_guess.lower() == "sten" or user_guess.lower() == "sax" or user_guess.lower() == "påse":
            pass
        else:
            print("Felaktig input, error 02")
            continue
        pass
    else:
        print("Felaktig input, error 01")
        continue
    rdy = input("Redo att köra? Y/N")
    print(rdy)
    if rdy.lower() != "y":
        print("Felaktig input, error 03")
        continue
    else:

        break

computor_choice = random.randint(1,3)


tie_breaker = False

tie_breaker = game_time(computor_choice, user_guess)





game_time(computor_choice, user_guess)



while tie_breaker ==True:
    tie_user_choice = input("Sten, sax, påse?: ")
    tie_computor_choice = random.randint(1,3)
    if tie_computor_choice == 1 and tie_user_choice == "påse":
        print("Användaren vinner")
        break
    elif tie_computor_choice == 3 and tie_user_choice == "sten":
        print("Datorn vinner")
        break
    elif tie_computor_choice == 2 and tie_user_choice == "påse":
        print("Datorn vinner")
        break
    elif tie_computor_choice == 3 and tie_user_choice == "sax":
        print("Användaren vinner")
        break
    elif tie_computor_choice == 1 and tie_user_choice == "sax":
        print("Datorn vinner")
        break
    elif tie_computor_choice == 2 and tie_user_choice == "sten":
        print("Användaren vinner")
        break

