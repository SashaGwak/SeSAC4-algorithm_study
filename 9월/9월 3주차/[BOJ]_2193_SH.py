# 2193(이친수)
'''
1 -> 1 (1)
2 -> 1 (10)
3 -> 2 (100, 101)
4 -> 3 (1001, 1010, 1000)
5 -> 5 (10000, 10001, 10010, 10100, 10101)
6 -> 8 (100000, 100001, 100010, 100100, 101000, 100101, 101001, 101010)
n = (n-1) + (n-2)
'''
N = int(input())

# 재귀는 시간초과뜨네영 
# def fivo(num): 
#     if num == 1 or num == 2:
#         return 1 
#     else:
#         return fivo(num-1) + fivo(num-2)

# print(fivo(N))

dp = [0, 1, 1]

for i in range(3, 91):
    dp.append(dp[i-1]+ dp[i-2])

print(dp[N])