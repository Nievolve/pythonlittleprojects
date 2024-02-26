year = int(input("Årskostnad: "))
basic = int(input("Enkelbiljett: "))
work_out = int(input("Hur många gånger per vecka: "))
work_out_year = work_out * 52
logic_1 = year / basic

if work_out_year > year:
    print("Inte värt att köpa årskort.")
    print(work_out_year)
    print(logic_1)
else:
    print("Det är värt att köpa ett årskort!")


