# 백준 2744 대소문자 바꾸기

str = input()
# 단어를 입력받는다.

new = ''
# 대문자를 소문자로, 소문자를 대문자로 변환해 저장할 변수를 만든다.

for char in str:
    if char.isupper() == 1:
        new += char.lower()

    else:
        new += char.upper()
# 입력받은 단어의 한 글자씩 불러오며 해당 글자가 대문자면 소문자로, 소문자면 대문자로 바꾸어 new 변수에 저장한다.

print(new)
# 새로 만든 문자열을 출력한다.
