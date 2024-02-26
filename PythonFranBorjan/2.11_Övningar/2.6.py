import math
def calculate_Nt(N0, t, t_half):
    Nt = N0 * (1/2) ** (t / t_half)
    return Nt
# Testa koden
N0 = int(input("Input 1: "))
t = 10    # Tiden
t_half = 5  # Halveringstiden
result = calculate_Nt(N0, t, t_half)
print(result)