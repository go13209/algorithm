input_word = input()

forbidden_char = [i for i in 'CAMBRIDGE']
new_word = ''
for char in input_word:
    if char not in forbidden_char:
        new_word += char
print(new_word)