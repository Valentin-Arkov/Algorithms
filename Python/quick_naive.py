def qsort(a):
    if len(a) <= 1:
        return a
    p = a[0]
    left = [x for x in a[1:] if x < p]
    right  = [x for x in a[1:] if x >= p]
    return qsort(left) + [p] + qsort(right)
a = [2, 1, 4, 6, 5, 3]
print(a)
print(qsort(a))

