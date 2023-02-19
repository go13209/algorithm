# 백준 3460 이진수

for t in range(int(input())):
    num = bin(int(input()))
    r_num = num[::-1]
    # 테스트 케이스 수를 입력받고 해당 수만큼 반복문을 돌린다.
    # 숫자를 입력받고 2진수로 변환하고 그 수를 뒤집는다.

    for i in range(len(r_num) - 2):
        if r_num[i] == '1':
            print(i, end=' ')
    # 2진수로 변환하면 접두어로 '0b'가 붙기 때문에 뒤집었을 때 마지막 두 글자를 제외한 배열만 불러온다.
    # 1의 위치를 출력한다.