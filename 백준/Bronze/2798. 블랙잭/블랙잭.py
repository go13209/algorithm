# 백준 2798 블랙잭
N, M = map(int, input().split())
# 카드의 개수 N과 게임의 기준이 되는 카드의 합 M을 입력받는다.

numbers = list(map(int, input().split()))
# 카드 숫자들을 입력받아 리스트에 저장한다.
total = 0
# M 이하의 가장 큰 카드의 합을 구하기 위해 'total'이라는 변수에 0을 저장한다.

for x in range(N-2):
    for y in range(x+1, N-1):
        for z in range(y+1, N):
            if total < numbers[x]+numbers[y]+numbers[z] <= M:
                total = numbers[x]+numbers[y]+numbers[z]
# 삼중 for문을 통해 카드의 값들을 하나씩 물러온다.
# 카드의 합이 M보다는 같거나 작되 가장 큰 카드의 합을 total 변수에 저장한다.

print(total)
# total 값을 출력한다.