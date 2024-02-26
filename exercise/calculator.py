number1 = float(input("Number: "))
agg = input("+-x/  ")
number2 = float(input("Number: "))
number3 = 0
if agg == "+":
    number3 = number1 + number2
else:
    pass
if agg.upper() == "X":
    number3 = number1 * number2
else:
    pass
if agg == "/":
    number3 = number1 / number2
else:
    pass
if agg == "-":
    number3 = number1 - number2
else:
    pass
print(number3)