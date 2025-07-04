import time

def sort(x):
  n = len(x)
  if n < 2:
    return x
  else:
    mid = n//2
    left = sort(x[:mid])
    right = sort(x[mid:])
    return merge(left, right)
    
def merge(left, right):
  i = j = 0
  s = []
  len_left = len(left)
  len_right = len(right)
  while i < len_left and j < len_right:
    if left[i] <= right[j]:
      s.append(left[i])
      i += 1
    else:
      s.append(right[j])
      j += 1
  s += left[i:] + right[j:]
  return s

print("n;T(n)")
for _ in range(10):
    for n in range(20000, 200001, 20000):
        x = list(range(n,0,-1))
        start = time.time()
        sort(x)
        end = time.time()
        tn = end - start
        print(f"{n};{tn:.10f}".replace(".",","))

#   10000, 0.0229725838
#  100000, 0.2744903564
#  200000; 0,6102993488
# 1000000, 3.2439601421