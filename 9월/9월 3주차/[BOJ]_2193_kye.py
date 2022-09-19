import sys
input = sys.stdin.readline()

n = int(input())
# 범위 설정
dp = [0] * (n+1)

dp[1] = 1
# dp[2] = 1     # 값 10만 되니까 dp[2] = 1 될 것 같은데 에러 뜸

for i in range(2, n+1):   
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
