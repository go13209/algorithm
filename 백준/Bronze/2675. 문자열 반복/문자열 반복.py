T = int(input())
for t in range(T):
    new_str = ''
    a, b = input().split()
    for char in b:
        new_str += char * int(a)
    print(new_str)