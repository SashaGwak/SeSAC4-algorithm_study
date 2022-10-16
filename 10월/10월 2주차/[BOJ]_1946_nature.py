# 1946 신입 사원

import sys

T = int(sys.stdin.readline()) # 테스트 케이스의 개수

for i in range(T):
    N = int(input()) # 지원자의 숫자
    A = [ ] # 지원자의 서류심사 성적, 면접 성적의 순위를 담을 빈 리스트
    for j in range(N):
        x, y = map(int, sys.stdin.readline().split())
        A.append([x, y])
    A.sort() # 숫자 리스트 정렬

    L = A[0][1] # 지원자의 서류심사 성적 1위의 면접 성적의 순위
    index = 1
    for j in range(1, N):
        if A[j][1] < L: 
            L = A[j][1]
            index += 1
    print(index)