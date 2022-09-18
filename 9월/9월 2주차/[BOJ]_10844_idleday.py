# 쉬운 계단 수 (10844)

# 시도1 -> 틀림 (뒷자리가 9로 끝나는 예외케이스 모두 고려하지X)
# def dp(N):
#     if N == 1:
#         return (9)
#     else:
#         return dp(N-1)*2-1

# 시도2
# 계단수가 N자리일때, 각 뒷자리숫자당 계단수 갯수count
# ^ N = 1   2   3   4  ..
# 0     0   1   1   3
# 1     1   1   3   4
# 2     1   2   3   7
# 3     1   2   4   7
# 4     1   2   4   8
# 5     1   2   4   8
# 6     1   2   4   8
# 7     1   2   4   7
# 8     1   2   3   6
# 9     1   1   2   3
# sum   9   17  32  56 ..


# N자리 계단수
N = int(input())

# dp는 2차원배열 (n*10)
# 인덱스: [N-1][뒷자리숫자]
dp = [[0] * 10 for _ in range(N)]

# N=1일 때, 각 뒷자리숫자당 계단수 갯수 1로 초기화
for i in range(1, 10):
    dp[0][i] = 1

# N=2 이상일때, 각 뒷자리숫자당 계단수 갯수
for i in range(1, N):
    # 뒷자리가 0이나 9인 예외케이스
    dp[i][0] = dp[i-1][1]  # (N-1일때) 뒷자리가 1인 갯수
    dp[i][9] = dp[i-1][8]  # (N-1일때) 뒷자리가 8인 갯수

    # 뒷자리가 1~8인 경우
    for j in range(1, 9):  # (N-1일때) j가 뒤에 올 수 있는 뒷자리들의 갯수 더하기
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


# 계단수 총합
sum = 0
for i in range(10):
    sum += dp[N-1][i]
print(sum % 1000000000)
