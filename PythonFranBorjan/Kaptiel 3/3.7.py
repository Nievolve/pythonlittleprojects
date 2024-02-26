kontant = 0
normal = 0
plus = 0

uppskattad = int(input("Antal minuter uppskattat per månad: "))

if uppskattad <= 32:
    print("Kontant abonnemanget är bäst för dig")
elif uppskattad >=67:
    print("Plus abonnemanget är bäst för dig")
else:
    print("Normal abonnemanget är bäst för dig")