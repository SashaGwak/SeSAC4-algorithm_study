# 나무 자르기 
import sys
N, M = map(int, input().split())
trees = list(map(int,sys.stdin.readline().split()))
start, end = 1, max(trees)

# start와 end가 같아질 때까지 반복
while start <= end: 
    mid = (start + end) // 2 # 중간 위치
    print(mid)

    count = 0 # 벌목된 나무 총합 

    # 나무 자르기 
    for tree in trees:
        # 나무의 높이가 절단기 높이 보다 크다면  
        if tree >= mid: 
            # 자르기 
            count += tree - mid
            print(count)

    # 자른 나무들의 길이가 목표값 이상이라면 
    if count >= M: 
        # 시작점 조정
        start = mid + 1
        print(start)
        print(end)
    # 목표값 이하라면
    else: 
        # 끝점 조정
        end = mid - 1 
        print(start)
        print(end)
    
print(end)
