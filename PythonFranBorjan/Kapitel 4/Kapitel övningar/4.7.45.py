# 2022= 26000
#föddes + 0.7
#döda - 0,6
#inflytt +300
#utflytt - 325
befolkning = 26000
current_befolkning = 26000
while True:
    year = int(input("År: "))
    if year < 2022:
        print("Error")
        break
    year_fix = year -2022
    for k in range (0, year_fix):

        current_befolkning = current_befolkning -25 * 1.01
    break
diff = befolkning - current_befolkning
print("År ", year, "kommer befolkningsmängden vara", current_befolkning, ". Vilket är en minskning på ", diff, "personer")
