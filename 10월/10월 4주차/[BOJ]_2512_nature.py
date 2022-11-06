# 2512 예산 

import sys
input = sys.stdin.readline

N = int(input()) # 지방의 수 N
J = list(map(int, input().split())) # 각 지방의 예산 요청을 표현하는 N개의 정수
M = int(input()) # 총 예산 M
start, end = 0, max(J) # 시작 점, 끝 점 

while start <= end:
    center = (start+end) // 2
    total = 0 # 총 지출 양
    for i in J:
        if i > center:
            total += center
        else:
            total += i
    if total <= M: # 지출 양이 예산보다 작으면 
        start = center + 1
    else: # 지출 양이 예산보다 크면 
        end = center - 1

print(end)       
