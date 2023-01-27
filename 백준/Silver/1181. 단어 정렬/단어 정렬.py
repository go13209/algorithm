N = int(input())
set = set()
words = []

for _ in range(N):
    string = input()
    set.add(string)
for str in set:
    words.append((len(str), str))

for length, word in sorted(words, key=lambda x: (x[0], x[1])):
    print(word)