# 16401 과자 나눠주기 

import sys

# 조카의 수 M, 과자의 수 N
M, N = map(int, sys.stdin.readline().split())

# 과자의 길이 
arr = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(arr)

result = 0

while (start <= end):
    total = 0
    center = (start + end) // 2

    # 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없을 때 
    if center == 0:
        total = 0
        break

    for i in arr:
        if i >= center:
            total += (i // center)
    
    if total >= M:
        start = center + 1
        result = center 
    
    else:
        end = center - 1
    
print(result)