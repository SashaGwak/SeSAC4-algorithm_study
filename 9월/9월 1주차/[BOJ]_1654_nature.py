#1654 랜선 자르기

import sys
K, N = map(int, input().split()) # K = 4, N = 11
list = [int(sys.stdin.readline()) for i in range(K)] # 802, 743, 457, 539

left = 1
right = max(list) 

while left <= right : 
    mid = (left + right) // 2 # 중간값
    lan = 0 #랜선 수

    for i in list:
        lan += i // mid # 중간값의 크기로 잘라냈을 때 몇개의 랜선이 모이는지
        
    if lan >= N: # 잘라낸 랜선의 수가 11보다 많다면 중간값보다 더 큰 숫자로 잘라서 랜선의 수를 줄이기
        left = mid + 1
    else: # 잘라낸 랜선의 수가 11보다 적다면 중간값보다 더 작은 숫자로 잘라서 랜선의 수를 늘리기
        right = mid - 1
print(right)