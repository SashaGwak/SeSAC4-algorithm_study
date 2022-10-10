# 수 길이 N
N = int(input())

# 범위 지정 
DP = [[0]*10 for _ in range(N+1)]

# 초기값 DP[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
DP[1] = [1] * 10

for i in range(2, N+1): 
    DP[i][0] = 1    # 끝자리 수 0 일 때 -> dp[1][0] = 0, dp[2][0] = 00, dp[3][0] = 000 이기 때문에 1 로 지정한다.
    for k in range(10):
        DP[i][k] = DP[i-1][k] + DP[i][k-1]
        # ex) 길이가 2, 끝자리 수가 5인 DP[2][5] = DP[1][5] + DP[2][4]
            
print(sum(DP[N]) %10007)
