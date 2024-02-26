while True:
    hojd = int(input("Höjd?: "))
    if hojd < 0:
        break
    bounce = 0
    current = hojd
    while current > 0.01:
        current = current * 0.7
        bounce += 1



    print("Det tog ", bounce, " gånger för bollen att stanna")
