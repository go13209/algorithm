import sys

dict = {}
for n in range(1, 10):
    number = int(sys.stdin.readline())
    dict[number] = n
new_dict = sorted(dict)
print(f'{sorted(dict)[8]}\n{dict[sorted(dict)[8]]}')