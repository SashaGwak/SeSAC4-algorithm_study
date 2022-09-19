# 11053 가장 긴 증가하는 부분 수열
import sys
import collections
input = sys.stdin.readline

N = int(input()) # 수열 크기
dp = collections.defaultdict(int) # 데이터 저장
stack = []
arr = list(map(int, input().split())) # 수열 정보 얻기

for i in range(N): # dp 1로 초기화
    dp[i] = 1

# arr 탐색
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1) # dp 갱신

print(max(dp.values()))