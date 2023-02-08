# 백준 11718 그대로 출력하기

while True:
    try:
        print(input())
    except EOFError:
        break

# 해당 문제는 몇 줄의 입력을 받는지 정해져 있지 않다.
# 이 경우 while 반복문을 사용해야 하지만 EOFError가 발생할 수 있다.
# EOFError란 더 이상 input으로 받아올 입력값이 없어 파일의 끝(End of File)에 도달했을 경우에 발생한다.
# 따라서 이 문제는 예외 처리 코드를 이용해 오류가 발생할 경우 반복문을 멈춰져야 한다.
