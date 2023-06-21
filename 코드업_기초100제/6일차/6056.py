# 코드업 파이썬 기초 100제
# 6056

a, b = map(int, input().split())
print((bool(a) and not bool(b)) or (not bool(a) and bool(b)))