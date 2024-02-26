meter_1 = float(input("Mätarinställnin idag?: "))
meter_2 = float(input("Mäterinställning för 1 år sedan?: "))
bensin_1 = float(input(" Liter bensin förbrukat: "))

driven = meter_1 - meter_2
bensin_2 = bensin_1 / driven

print(f"Anta körda mil: {driven:.1f}")
print(f"Bensinförbrukning per mil {bensin_2:.1f}")