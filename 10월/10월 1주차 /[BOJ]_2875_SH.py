# 2875 대회 or 인턴
from math import ceil
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

# 팀 수 
count = 0

# 일단 최대한 많은 팀 만들기 
while True: 
    N -= 2   
    M -= 1 
    if N < 0 or M < 0 or (N + M) < K: 
        break
    count += 1 

print(count) 