word = list(input())
N = len(word)
lst = []

for i in range(N-2):
    first = word[i::-1]
    for j in range(i+1, N-1):
        second = word[j:i:-1]
        for k in range(j+1, N):
            third = word[:j:-1]
            reversed_word = first + second + third
            lst.append(''.join(reversed_word))

print((sorted(lst))[0])