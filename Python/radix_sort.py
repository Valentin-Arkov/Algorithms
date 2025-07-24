def rsort(a):
    max_len = max(len(str(x)) for x in a)
    b = 10
    for i in range(max_len):
        t = [[] for _ in range(b)]
        for x in a:
            d = (x // (b ** i)) % b
            t[d].append(x)
        a = [z for x in t for z in x]
        print(f'{i}: {t}')
        print(f'{i}: {a}')
    return a
a = [31, 2, 321, 124, 12, 330, 211, 4]
print(f'a: {a}')
print(f'a: {rsort(a)}')

