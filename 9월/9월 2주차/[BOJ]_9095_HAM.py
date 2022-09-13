import sys
input = sys.stdin.readline

T = int(input())

# 풀이 1
cache = [0] * 11
# 범위가 10까지이므로 미리 값들을 모두 구하고 
# (근데 왜 11까지 만드는거지?)

cache[1] = 1
cache[2] = 2
cache[3] = 4
# 초기값 1, 2, 3 경우까지 캐시에 미리 넣어주기

for i in range(4, 11) :
    cache[i] = sum(cache[i-3:i])
    # i부터 이전 3개까지 합산을 구한다.

for _ in range(T) :
    print(cache[int(input())])


# 풀이 2
for i in range(T) :
    n = int(input())
    dp = [0] * (n+1)
    if n == 1 :
        print(1)
    elif n == 2 :
        print(2)
    elif n == 3 :
        print(4)
    else :
        dp[1] = 1
        dp[2] = 2
        dp[4] = 4

        for j in range(4, n+1) :
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        print(dp[n])