import math

punk_01x = int(input("Skriv in X1: "))
punk_01y = int(input("Skriv in Y1: "))
punk_02x = int(input("Skriv in X2: "))
punk_02y = int(input("Skriv in Y2: "))


position = math.sqrt((punk_01x-punk_02x)**2 + (punk_01y-punk_02y)**2)

print(f"{position:.2f}")