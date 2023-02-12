# 백준 11866 요세푸스 문제

from collections import deque

N, K = map(int, input().split())
# 사람의 수 N과 몇 번째 사람을 제거할 것인지 K를 입력받는다.

nums = deque([i for i in range(1, N + 1)])
# 덱 기능을 사용하기 위해 1번부터 N 번까지의 사람을 덱으로 만든다.

del_nums = []
# 제거되는 사람들의 순서를 저장하기 위해 빈 리스트를 만든다.

while nums:
    for _ in range(K - 1):
        nums.append(nums.popleft())
    # K 번째 사람을 제거하기 위해 그 앞 사람들은 제거했다가 다시 덱 끝에 넣는다.

    del_nums.append(nums.popleft())
    # K번째 사람을 제거해 del_nums 리스트에 넣는다.
    # 이 과정을 모든 사람이 제거될 때까지 반복한다.

print('<', ', '.join(map(str, del_nums)), '>', sep='')
# 제거된 사람들의 순서를 출력한다.
