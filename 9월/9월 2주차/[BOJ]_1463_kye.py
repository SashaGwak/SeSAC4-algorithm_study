# 문제
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

n = int(input())

# n+1개 범위 만큼의 0으로 이루어진 배열을 만든다. 
dp = [0] * (n+1)  

# dp[1] = 0 이므로 2를 시작점으로 한다.
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])

# 점화식: dp(N) = min( dp(N//3)+1, dp(N//2)+1, dp(N-1)+1 )
# 배열 dp = 인덱스 n을 1로 만드는 최소 연산의 횟수
# n이 2, 3의 배수가 아닐 때, n에서 1을 뺀다. 예를 들어 n=7일 때, n에서 1을 빼면 6이 되고, 6을 1로 만드는 연산은 n=6일 때의 연산값과 같다. 
# 다시 말해, n=7일 때 n에서 1을 빼는 연산 횟수 1번 + 6을 1로 만드는 dp[6] 값을 더하면 dp[7] 값을 구할 수 있다. dp[7] = 1 + dp[6]
