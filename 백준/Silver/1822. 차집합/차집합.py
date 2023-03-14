A, B = map(int, input().split())
A_nums = set(map(int, input().split()))
B_nums = set(map(int, input().split()))

difference = sorted(A_nums - B_nums)
print(len(difference))
print(*difference)