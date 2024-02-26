import math
a = float(input("Sida A: "))
b = float(input("Sida B: "))
v = float(input("Vinkeln: "))

r = (v * math.pi)/180   ##Räkna ut radierna. (Vinkeln * Pi/180) I detta fall är blir resultatet uttryckt i radierna, Pi/4
print(r)
c = math.sqrt(a**2+b**2-2*a*b * math.cos(r))
print(c)

radians = (v * math.pi)/180
d = math.sqrt(a**2 + b**2 - 2*a*b * math.cos(radians))
print(d)
v_a = 0
v_b = 0
v_c = 0


print(f"Sida A är {a:.0f} sida B är {b:.0f} och sida C är {c:.0f}")