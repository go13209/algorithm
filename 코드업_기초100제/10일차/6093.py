# 코드업 파이썬 기초 100제
# 6093

n = int(input())
nums = list(map(int, input().split()))
print(*nums[::-1])