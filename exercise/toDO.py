


def show1(todo1):
    for rem1 in todo1:
        print(rem1)

def welc2(welc1):
    for pri1 in welc1:
        print(pri1)

welc1 = ["Welcome", "This is the main menu", "With four options.", "1. Add", "2. Remove", "3. Show", "4. End"]

todo1 = []

while True:
    welc2(welc1)
    val1 = int(input("Choose:  "))

    if val1 ==  1:
        print("Type to add?")
        appe1 = input(" ")
        todo1.append(appe1)

    elif val1 == 2:

       print("Type to remove?")
       show1(todo1)
       dele1 = input(" ")
       todo1.remove(dele1)

    elif val1 ==3: #Lägga till nån stopp här
        show1(todo1)
        print("Press any key")
        any1 = input(" ")
        pass
    elif val1 == 4:
        print("End program...")
        break

    else:
        print("Error")
