def find_max(nums):
    max_num = nums[0]
    for i in range(1, len(nums)):
        if max_num < nums[i]:
            max_num = nums[i]
    return max_num
import time
print("n;T(n)")
for n in range(20_000_000, 100_000_001, 20_000_000):
    nums = n * [1]
#   nums = [2] + (n - 1) * [1]
    for i in range(10):
        t = time.perf_counter()
        x_max = find_max(nums)
        dt = time.perf_counter() - t
        print(f"{n};{dt:.10f}".replace(".",","), flush=True)
# (cc) Арьков В.Ю.