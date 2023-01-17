total = 1
for t in range(3):
    number = int(input())
    total *= number

dict = {}
for i in range(10):
    dict[str(i)] = 0

for n in str(total):
    if n in dict.keys():
        dict[n] += 1

for v in dict.values():
    print(v)