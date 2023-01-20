T = int(input())

for t in range(1, T + 1):
    str = input()
    reversed_word = ''
    for char in str[::-1]:
        reversed_word += char
    if str == reversed_word:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')