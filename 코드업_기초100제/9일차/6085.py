# 코드업 파이썬 기초 100제
# 6085

w, h, b = map(int, input().split())
print(format(w*h*b/8/1024/1024, '.2f'), 'MB')