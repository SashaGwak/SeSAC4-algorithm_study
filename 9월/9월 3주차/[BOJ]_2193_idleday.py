# 2193(이친수)

# n자리 이친수
n = int(input())

# dp는 n자리수 배열 (n은 1이상 90이하)
dp = [0] * (91)

# n=1일때 1
dp[1] = 1

# n=2일때 10
dp[2] = 1

# n=3일때 100,101
dp[3] = 2

# n=4일때 1000, 1001, 1010
dp[4] = 3


# 점화식
for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])