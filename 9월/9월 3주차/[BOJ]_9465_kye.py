import sys
input = sys.stdin.readline()

# 테스트 케이스의 개수 t
t = int(input())

for _ in range(t):
    n = int(input()) # n 정수 개수
    dp = [list(map(int, input().split())) for _ in range(2) ] # range(2)를 걸어 두 개의 dp 배열을 만든다  
    dp[0][1] += dp[1][0] # 대각선 방향의 값 중 최댓값을 구하는 건 알겠는데 이건 왜 필요한걸까.. 
    dp[1][1] += dp[0][0]
    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][n-1], dp[1][n-1]))
 
# 참고한 글 복붙
# dp[0][3] 이 최대가 되려면 dp[1][2] 를 선택하거나 dp[1][1] 을 선택해야 한다. 
# dp[1][1] 을 선택시 그 오른쪽옆인 dp[1][2] 는 당연히 선택이 안될 것이고, dp[0][3] 의 왼쪽 옆인 dp[0][2] 도 선택이 안될 것이다.
# 따라서 그 열까지의 최댓값을 구하려면 dp[0][i]이면 dp[1][i-1] 과 dp[1][i-2] 중 큰 값을 자기 자신과 더하고, dp[1][i]이면 dp[0][i-1] 과 dp[0][i-2] 중 큰 값을 자기 자신과 더하면 된다. 
# 즉, 자신의 자리에서 전 열의 대각선 또는 전전 열의 대각선 둘 중 큰 값과 자신을 더한 값이 항상 최대가 될 것이다.
# 그리고 그 열의 최댓값은 dp[0][n] 과 dp[1][n] 둘 중 큰 값으로 정하면 된다.
