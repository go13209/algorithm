# 코드업 파이썬 기초 100제
# 6065

numbers = list(map(int, input().split()))
for number in numbers:
    if number % 2 == 0:
        print(number)
