N = list(map(int, input().split()))

while True:
    for n in range(len(N)-1):
        if N[n] > N[n + 1]:
            N[n], N[n + 1] = N[n + 1], N[n]
            print(*N)
    if N == [1, 2, 3, 4, 5]:
        break