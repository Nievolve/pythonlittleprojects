import datetime
input_time_1 = input("Tid 1 (TT:MM) : ").replace(":", "").replace(" ", "")
input_time_2 =  input("Tid 2 (TT:MM) : ").replace(":", "").replace(" ", "")
tid_now_1_hour = int(input_time_1[:2]) # int
tid_now_1_minute = int(input_time_1[2:4]) # int
tid_now_2_hour = int(input_time_2[:2]) # int
tid_now_2_minute = int(input_time_2[2:4]) # int
dt = datetime.datetime.now()
tid = dt.time()

print(tid_now_1_hour, ":", tid_now_1_minute)
print(tid_now_2_hour, ":", tid_now_2_minute)

antal_min_1 = tid_now_1_hour * 60 + tid_now_1_minute
antal_min_2 = tid_now_2_hour * 60 + tid_now_2_minute

print(antal_min_1-antal_min_2)





