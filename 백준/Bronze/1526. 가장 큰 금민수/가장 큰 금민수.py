N = int(input())
lst = []

for i in range(N+1):
    i = str(i)
    if i.count('4') + i.count('7') == len(i):
        lst.append(int(i))
print(max(lst))