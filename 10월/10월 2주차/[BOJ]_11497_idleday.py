# 11497 통나무 건너뛰기
import sys
T = int(sys.stdin.readline())   # 테스트 케이스 개수 입력

for _ in range(T):
    N = int(sys.stdin.readline())   # 통나무 개수 입력

    # 통나무를 높이 순서대로 정렬
    heights = sorted(list(map(int, sys.stdin.readline().split())))
    # heights = list(map(int,sys.stdin.readline().split()))
    # heights.sort()


# n개의 통나무가 있을 때, 인접하는 통나무 사이의 최대 높이차는 n-2번과 n번의 높이차
    result = 0  # 높이차 기록
    for i in range(2, N):  # 2부터 N까지, index가 2개 차이날 때의 높이차 중 최댓값을 result에 기록
        result = max(result, abs(heights[i] - heights[i - 2]))
    print(result)
