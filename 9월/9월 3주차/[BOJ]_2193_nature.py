#2193 이친수

N = int(input())

# memoization
dp = [0] * 91
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])