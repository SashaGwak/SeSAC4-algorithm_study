# 2*n 타일링 2(11727)
'''
2*N 
2*1 -> 1 
2*2 -> 3 
2*3 -> 5 
2*4 -> 11 
2*5 -> 21 
(n-1)+2(n-1)
'''
n = int(input())
dp = [1, 3, 5]

for i in range(3, 1001): 
    dp.append(dp[i-2]*2 + dp[i-1])

print(dp[n]%10007)