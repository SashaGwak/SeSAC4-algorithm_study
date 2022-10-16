# 11497 통나무 건너뛰기

import sys

T = int(sys.stdin.readline()) # 테스트 케이스 수

for i in range(T):
    N = int(sys.stdin.readline()) # 통나무의 개수를 나타내는 정수
    L = [int(x) for x in sys.stdin.readline().split()] # 각 통나무의 높이를 나타내는 정수
    L.sort() # 통나무의 높이별로 정렬

    M = 0 # 난이도

    for i in range(2, N): # 2부터 N까지 인덱스를 2로 차이를 두어서 값을 구함
        M = max(M, abs(L[i] - L[i-2])) # abs : 절대값

    print(M)


