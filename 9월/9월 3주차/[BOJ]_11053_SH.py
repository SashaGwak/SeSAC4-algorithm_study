# 가장 긴 증가하는 부분 수열(11053)
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [0 for i in range(N)] 
print('디피느 ㄴ머냐면', dp)

for i in range(N): # 현재 인덱스 
    print('아이',i)
    for j in range(i): # 인전 리스트 인자들과 비교 
        print('제이', j)
        print('A[i]!!!', A[i])
        print('A[j]!!!', A[j])
        if A[i] > A[j] and dp[i] < dp[j]: # 현재 인덱스가 앞에보다 크고, 전의 
            print('여기가 더하기 전', dp)
            dp[i] = dp[j]
            print('디피아잇', dp[i])
            print('디피제에에에에에에에에이', dp[j])

        dp[i] += 1
        print('여기가 더하기 후후후후후후후ㅜ불면은 ', dp)

print(max(dp))