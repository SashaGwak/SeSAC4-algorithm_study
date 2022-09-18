#11057 오르막 수

N = int(input())

dp = [1] * 10

for i in range(N-1):
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(sum(dp)%10007)

# 0으로 끝나는 숫자
# 0 -> 1

#1로 끝나는 숫자
#1 -> 1, (01, 11 -> 2), (001, 011, 111 -> 3)

#2로 끝나는 숫자
#2 -> 1, (02, 12, 22 -> 3), (002, 012, 022, 112, 122, 222 -> 6)

# 1로 끝나는 숫자 두번째(01, 11 ->2) + 2로 끝나는 숫자 첫번째(2 -> 1) = 2로 끝나는 숫자 두번째(02, 12, 22 -> 3)
# 1로 끝나는 숫자 세번째(001, 011, 111 -> 3) + 2로 끝나는 숫자 두번째(02, 12, 22 -> 3) = 
# 2로 끝나는  숫자 세번쨰(002, 012, 022, 112, 122, 222 -> 6) 

# 즉, dp[j] += dp[j-1]