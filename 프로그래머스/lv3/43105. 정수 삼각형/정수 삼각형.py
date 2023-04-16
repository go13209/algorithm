def solution(triangle):
    dp = [[0 for _ in range(i+1)] for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        dp[i][0] = triangle[i][0] + dp[i-1][0]
        dp[i][-1] = triangle[i][-1] + dp[i-1][-1]

        for j in range(1, i):
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    
    return max(dp[-1])