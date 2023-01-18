T = int(input())
for t in range(T):
    a, b = map(str, input().split())
    new_word = ''
    for char in b:
        new_word += char * int(a)
    print(new_word)