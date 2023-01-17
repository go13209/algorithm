T = int(input())
for t in range(T):
    N = int(input())
    list = [n for n in map(int, input().split())]
    print(sum(list))