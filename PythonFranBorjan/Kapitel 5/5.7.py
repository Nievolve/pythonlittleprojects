a = "Erik Andersson 990314-2714"


b =a.find("0")
c = a.find("9")
d = a.find ("1")
year = a[c:c+2]
month = a[b:b+2]
day = a[d:d+2]


print(year)
print(month,"/", end="")
print(day)
