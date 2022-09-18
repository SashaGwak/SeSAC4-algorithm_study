# 2 x n 타일링 (11726)
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수

# n=1 -> 1
# n=2 -> 2
# n=3 -> 3
# n=4 -> 5
# n=5 -> 8
# 규칙: dp[n] = dp[n-1] + dp[n-2]


# 입력
n = int(input())


# ^ memoization 1
dp = [0, 1, 2]
# DP 1
for i in range(3, 1001):    # for i in range(3, n + 1):
    dp.append(dp[i - 2] + dp[i - 1])


# ^ memoization 2
dp = [0] * 1001     # dp = [0]*(n+1) # dp = [0 for _ in range(n+1)]
dp[1] = 1
dp[2] = 2
# DP 2
for i in range(3, 1001):    # for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2])


# 결과 출력
print(dp[n] % 10007)
