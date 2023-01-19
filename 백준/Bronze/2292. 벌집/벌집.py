N = int(input())

honeycomb = 1
group = 1

while N > honeycomb:
    honeycomb += group * 6
    group += 1

print(group)