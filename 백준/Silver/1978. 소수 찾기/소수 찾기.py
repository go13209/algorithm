# 백준 1978 소수 찾기

N = int(input())
# 수의 개수를 입력받는다.

nums = list(map(int, input().split()))
# 입력받은 수들을 리스트로 저장한다.

cnt = 0
# 소수의 개수를 세기 위한 변수를 만든다.

for i in range(N):
    num = nums[i]
    n = 1
    divisor = []
    while n <= num:
        if num % n == 0:
            divisor.append(n)
            n += 1
        else:
            n += 1
    # 1부터 시작해서 해당 수를 나누었을 때 나누어떨어지는 수를 divisor(약수) 리스트에 저장한다.

    if len(divisor) == 2:
        cnt += 1
    # divisor 리스트의 요소가 2개라는 것은 1과 자기 자신밖에 없다는 의미이므로 소수에 해당한다.
    # 따라서 cnt 변수에 1을 더한다.

print(cnt)
# 소수의 개수를 출력한다.
