T = int(input())

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(1, T+1):
    N, K = map(int, input().split())
    scores = []

    for n in range(N):
        mid, final, task = map(int, input().split())
        scores.append([n+1, mid*0.35 + final*0.45 + task*0.2])

    cnt = 0
    grade_num = 0
    for score in sorted(scores, key = lambda x:x[1], reverse=True):
        score[1] = grade[grade_num]
        cnt += 1
        if cnt == N // 10:
            grade_num += 1
            cnt = 0

    print(f'#{t} {scores[K-1][1]}')