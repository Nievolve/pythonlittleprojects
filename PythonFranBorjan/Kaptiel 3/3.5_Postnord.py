print("Skriv in längd, bredd och djup i mm.")
while True:
    l = int(input("Längd: "))
    b = int(input("Bredd: "))
    t = int(input("Djup: "))

    if l >= 140 and l <= 600 and \
       b >= 90 and b <= 100 and \
       t >= 100 and t <= 900:

        print("Paketet ser najs ut.")
        break
    else:
        if l > 600 or l < 140:
            print(l)
            print("Ogiltig längd")
        elif b < 90 or b > 100:
            print(b)
            print("Ogiltig bredd")

        elif t < 100 or t > 900:
            print(t)
            print("Ogiltig djup")