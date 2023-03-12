import sys

A, B = list(sys.stdin.readline().split())
rev_A = int(A[::-1])
rev_B = int(B[::-1])
rev_answer = int(str(rev_A + rev_B)[::-1])
print(rev_answer)