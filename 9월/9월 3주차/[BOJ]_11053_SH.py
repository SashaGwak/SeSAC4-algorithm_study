# 가장 긴 증가하는 부분 수열(11053)
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N 
print('디피느 ㄴ머냐면', dp)

for i in range(1, N): # 현재 인덱스 
    print('아이',i)
    for j in range(i): # 인전 리스트 인자들과 비교 
        print('제이', j)
        print('A[i]!!!', A[i])
        print('A[j]!!!', A[j])
        if A[i] > A[j]: # 뒤에나오는게 더 크면
            ㅔ
            dp[i] = max(dp[i], dp[j]+1)
            print('디피아잇', dp[i])
            print('디피제에에에에에에에에이', dp[j] + 1)



print(max(dp))