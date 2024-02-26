import math

radie = int(input("Ange radie: "))

area = 4 * math.pi * radie ** 2

volym = 4 * math.pi * radie ** 3 / 3

print(f"Arean är: {area:.3f}. Avrundat blir det: {area:.1f}")
print(f"Volymen är: {volym:.3f}. Avrundat blir det: {volym:.1f}")

