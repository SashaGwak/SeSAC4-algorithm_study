n = int(input())

#범위 설정
dp = [0] * 1001

#초기값 
dp[0] = 1
dp[1] = 1

# 점화식: dp[n] = (n-1) + (n-2)*2
for i in range(2, 1001):
    dp[i] = dp[i-1] + dp[i-2]*2
    
print(dp[n]%10007)