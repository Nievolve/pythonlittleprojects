miles = int(input("Ange miles: "))
gallon = int(input("Ange gallon: "))

km = miles * 1.609
liter = gallon * 3.785

print(f"Uträknat är det {km:.2f} och {liter:.2f}")