from collections import deque

for t in range(1, 11):
    N = int(input())
    numbers = deque(list(map(int, input().split())))
    minus = 1
    while True:
        if minus > 5:
            minus = 1
        numbers.append(numbers[0] - minus)
        numbers.popleft()
        if numbers[-1] <= 0:
            numbers[-1] = 0
            break
        minus += 1
    
    number = ''
    for num in numbers:
        number += str(num) + ' '
    print(f'#{t} {number}')