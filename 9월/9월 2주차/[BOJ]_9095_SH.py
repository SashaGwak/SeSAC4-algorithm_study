# 1,2,3 더하기(9095)
'''
n=0 -> 0 
n=1 -> 1
n=2 -> 2 
n=3 -> 4
n=4 -> 7
n=5 -> 13
(n-1)+(n-2)+1(n-3)
'''
T = int(input())
dp = [0, 1, 2, 4]
num = []

for i in range(4, 12): 
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    
for i in range(4, T+4): 
    n = int(input())
    num.append(n)

for i in num:
    print(dp[i])