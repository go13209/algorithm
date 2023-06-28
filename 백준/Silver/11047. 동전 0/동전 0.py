N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
cnt = 0

for i in sorted(coins, reverse=True):
    if i <= K:
        cnt += K // i
        K -= K // i * i
print(cnt)