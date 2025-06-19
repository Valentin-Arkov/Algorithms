def bubble(x):
    n = len(x)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x

x = [3, 2, 1, 4, 5]
print(x)
print(bubble(x))

# (c) Valentin Arkov
