# 백준 10101 삼각형 외우기
numbers = []
# 삼각형의 세 각을 저장할 빈 리스트 생성
for i in range(3):
    numbers.append(int(input()))
numbers.sort()
# 세 각을 입력받아 리스트에 저장하고 오름차순으로 정렬

if sum(numbers) != 180:
    print('Error')
# 세 각의 합이 180이 아닐 경우 Error 출력

else:
    if numbers[0] == numbers[1] and numbers[1] == numbers[2]:
        print('Equilateral')
    # 세 각이 모두 같으면 'Equilateral' 출력
    elif numbers[0] != numbers[1] and numbers[1] != numbers[2]:
        print('Scalene')
    # 세 각이 모두 다르면 'Scalene' 출력
    else:
        print('Isosceles')
    # 그 외의 경우 'Isosceles' 출력