total = int(input())
kind = int(input())
amount = 0
for N in range(0, kind):
    product_list = list(map(int, input().split()))
    amount += product_list[0] * product_list[1]
if amount == total:
    print('Yes')
else:
    print('No')