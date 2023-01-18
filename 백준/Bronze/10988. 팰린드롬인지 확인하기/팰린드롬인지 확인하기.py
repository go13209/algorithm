word = input()
reversed_word = ''
for char in word[::-1]:
    reversed_word += char
if reversed_word == word:
    print(1)
else:
    print(0)