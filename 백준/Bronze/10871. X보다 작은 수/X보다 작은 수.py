a, b = map(int, input().split())
numbers = list(map(int, input().split()))
for number in numbers:
    if number < b:
        print(number, end=' ')