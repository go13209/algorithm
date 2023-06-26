# 코드업 파이썬 기초 100제
# 6081

n = int(input(), 16)
for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')