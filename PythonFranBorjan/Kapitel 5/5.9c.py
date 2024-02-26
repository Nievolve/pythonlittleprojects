input = input(": ").replace(" ", "")
compare_2 = input[::-1]
if input == compare_2:
    print("Du har palindrom")
else:
    print("Du har inget palindrom")