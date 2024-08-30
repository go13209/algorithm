# 백준 17413 단어 뒤집기 2

string = input()
reversed_word = ""
result = ""
tag = False

for char in string:
    if char == "<":
        if reversed_word:
            result += reversed_word[::-1]
            reversed_word = ""
        tag = True
        result += char
    
    elif char == ">":
        tag = False
        result += char

    elif tag:
        result += char
    
    elif char == " ":
        result += reversed_word[::-1]
        result += char
        reversed_word = ""

    else:
        reversed_word += char

if reversed_word:
    result += reversed_word[::-1]

print(result)