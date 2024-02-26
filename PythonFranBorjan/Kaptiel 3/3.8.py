import math
while True:
    radie = float(input("Radie: "))

    area = radie**2 * math.pi
    omkrets = radie * 2 * math.pi

    if radie <= 0:
        print("Error. Value less then or equal to 0")
        print("Try again")
    else:
        break
print (f"{area:.3f} {omkrets:.3f}")