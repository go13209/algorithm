T = int(input())

for t in range(T):
    reversed_sentence = []
    sentence = input().split()
    for word in sentence:
        reversed_sentence.append(word[::-1])
    print(*reversed_sentence)