dict = {}
for n in range(1, 10001):
    dict[n] = n + sum(list(map(int, str(n))))
for key in dict.keys():
    if key not in dict.values():
        print(key)