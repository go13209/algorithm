num = list(map(int, input().split()))
divisor = []

n = 2
while n <= min(num):
    if num[0] % n == 0 and num[1] % n == 0:
        divisor.append(n)
        num[0] = num[0] // n
        num[1] = num[1] // n
        n = 2
    else:
        n += 1

GCD = 1

for i in divisor:
    GCD *= i

print(GCD)
print(GCD * num[0] * num[1])