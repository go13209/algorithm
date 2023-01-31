list = [int(input()) for _ in range(10)]
cnt = []
for num in set(list):
    cnt.append([num, list.count(num)])
cnt.sort(key=lambda x: (x[1], x[0]))
print(int(sum(list)/len(list)))
print(cnt[-1][0])