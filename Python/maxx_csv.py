# find maximum value in a list

# print out into csv
# python maxx_csv.py
# python maxx_csv.py > maxx_py_best.csv
# python maxx_csv.py | tee maxx_py_best.csv

def find_max(nums):
    return max(nums)

import time
print("n;T(n)")   # RU Excel
# print("n,T(n)") # EN Excel

for n in range(8_000_000, 40_000_001, 8_000_000):
    nums = n * [1]    # best case
#   nums = range(n)   # worst case
    for _ in range(10):
        t = time.perf_counter()
        x_max = find_max(nums)
        dt = time.perf_counter() - t
        print(f"{n};{dt:.10f}".replace(".",","), flush=True) # RU Excel
#       print(f"{n},{dt:.10f}", flush=True)                  # EN Excel
        
# (c) Valentin Arkov
