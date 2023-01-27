remainder = set()

for _ in range(10):
    number = int(input())
    remainder.add(number%42)
print(len(remainder))