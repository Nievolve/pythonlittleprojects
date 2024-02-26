vara = input(" Skriv in varans namn: ").lower() ##För att snygga till utskriften så görs stringen om till endast små bokstäver
brutto = float(input("Skriv in varans pris: "))
moms = float(input("Skriv in moms (%): "))
##Gör om talet som inputtades till ett tal some går att använda i arimetriska uträkningar
netto_moms = moms / 100
##Räknar ut hur står momsen blir på aktuella varan/pris
moms_to_pay = brutto * netto_moms
##Vad varan skulle kosta on det var exklusive moms
exl_moms = brutto - moms_to_pay

##Använder f.String för att placeholda variablar och begränsa antal decimaler. Igen för att snygga till utskriften så läggs stor bokstav till på varan
print("Varan", vara.capitalize(), " kostar" , brutto, f" kr. Med en moms på {moms_to_pay:.2f}. Exklusive moms skulle ", vara.capitalize(), f" kosta {exl_moms:.2f}")