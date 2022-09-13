# 1,2,3 더하기(9095)

# 점화식 규칙
def dp(n):
    # n=1 -> 1
    if n == 1:
        return 1
    # n=2 -> 1+1, 2
    elif n == 2:
        return 2
     # n=3 -> 3+1, 2+2, 2+1+1, 1+1+1+1
    elif n == 3:
        return 4
    else:           # n=4 -> 3+1, 2+2, 2+1+1, 1+1+1+1
        return dp(n-1)+dp(n-2)+dp(n-3)


# 테스트케이스 개수 T
T = int(input())

# 정수n (1~10) T번 입력받기
for i in range(T):
    n = int(input())
    print(dp(n))
