import datetime

dt = datetime.datetime.now()
tid = dt.time()
time = str(dt)[10:19]
datum = dt.date()
print(datum)
print(tid)
print(time)
