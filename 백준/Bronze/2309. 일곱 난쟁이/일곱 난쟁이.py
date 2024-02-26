from itertools import combinations

dwarfs = list()

for _ in range(9):
    height = int(input())
    dwarfs.append(height)

dwarfs = sorted(dwarfs)

for i in list(combinations(dwarfs, 7)):
    if sum(i) == 100:
        for j in i:
            print(j)
        break