import sys
input = sys.stdin.readline

n = int(input())
dp = [ 0 for _ in range(n+1)]


if n <= 3 : print(n)

else :
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1) :
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[i]%10007)

    #10007을 나눠주는 이유는
    # 문제에서 첫째 줄에 2*n 크기의 직사각형을 채우는
    # 방법의 수를 10,007로 나눈 나머지를 출력한다고 했기 떄문.
