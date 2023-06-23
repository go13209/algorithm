# 코드업 파이썬 기초 100제
# 6074

char = ord(input())
start = ord('a')
while start <= char:
    print(chr(start), end=' ')
    start += 1