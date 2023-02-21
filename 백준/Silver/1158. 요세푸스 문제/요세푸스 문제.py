# 백준 1158 요세푸스 문제

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
# 사람의 수 N과 몇 번째 사람을 제거해나갈지 숫자 K를 입력받는다.

lst = deque([i for i in range(1, N + 1)])
# 1~N까지의 리스트를 만들어 덱에 넣는다.

rm_lst = []
# 제거한 사람의 순서를 저장하기 위해 빈 리스트를 만든다.

while lst:
    for _ in range(K - 1):
        lst.append(lst.popleft())
    
    rm_lst.append(lst.popleft())
# K 번 전까지의 사람은 pop 해서 다시 뒤에 붙인다.
# K 번째 사람을 제거하고 빈 리스트에 저장한다.
# 이 과정을 모든 사람이 제거될 때까지 반복한다.

print('<' + ', '.join(map(str, rm_lst)) + '>', sep='')
# 제거한 사람의 순서를 출력한다.
