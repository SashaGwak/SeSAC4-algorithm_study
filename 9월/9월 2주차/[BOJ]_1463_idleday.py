# 1로만들기 (1463)


n = int(input())

# memoization
dp = [0 for _ in range(n+1)]
d = [0] * (n + 1)

# index == 입력(n)
# index값 == 출력(연산최솟값)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[n])
