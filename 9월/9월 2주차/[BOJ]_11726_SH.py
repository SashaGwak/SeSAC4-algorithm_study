# 2*n 타일링(11726)
'''
2*0 -> 0개
2*1 -> 1개
2*2 -> 2개 
2*3 -> 3개 
2*4 -> 5개 
2*5 -> 8개 
2*6 -> 13개 
n 방법 개수 = (n - 1)+(n -2) 
'''
# 3부터 시작하기 위해 dp[2]까지 값 넣어주기 
dp = [0, 1, 2]

for i in range(3, 1001):
    # n 방법 개수 = (n - 1)+(n -2) 실행 
    dp.append(dp[i - 2] + dp[i - 1])

n = int(input())

#  직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력하는 문제 값 
print(dp[n] % 10007)