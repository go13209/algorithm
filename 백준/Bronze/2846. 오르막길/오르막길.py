N = int(input())
height = list(map(int, input().split()))
uphill = []
gap = 0
for i in range(N-1):
    if height[i] < height[i+1]:
        gap += height[i+1] - height[i]
    else:
        uphill.append(gap)
        gap = 0
else:
    uphill.append(gap)

if len(uphill) == 0:
    print(0)
else:
    print(max(uphill))