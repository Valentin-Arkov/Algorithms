# find maximum value in a list
def find_max(nums):
    return max(nums)

import time

# choose n to get t = 0.1 ... 1.0 sec
n = 40_000_000
nums = n * [1]  # best case
# nums = range(n) # worst case
t = time.perf_counter()
x_max = find_max(nums)
dt = time.perf_counter() - t
print(n, dt)
        
# (c) Valentin Arkov
