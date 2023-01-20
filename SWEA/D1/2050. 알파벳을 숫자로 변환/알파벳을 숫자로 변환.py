str = input()
alphabet_dict = {}
value = 1
for alphabet in range(ord('A'), ord('Z') + 1):
    alphabet_dict[chr(alphabet)] = value
    value += 1

for char in str:
    print(alphabet_dict[char], end=' ')