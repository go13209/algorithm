# 백준 1037 약수

N = int(input())
num = sorted(list(map(int, input().split())))
# 진짜 약수의 개수 N을 입력받는다.
# 진짜 약수를 입력받고 오름차순으로 정렬된 리스트로 만든다.

answer = num[0] ** 2 if len(num) == 1 else num[0] * num[-1]
print(answer)
# 1과 N을 제외한 진짜 약수의 개수가 한 개일 경우 해당 약수를 제곱한 수를 출력한다.
# 진짜 약수의 개수가 두 개 이상일 경우 정렬된 리스트의 첫 번째 수와 제일 마지막 수를 곱한 값을 출력한다.
