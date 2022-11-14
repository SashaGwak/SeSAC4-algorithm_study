# 2231 분해합
# 브루트포스 알고리즘 (완전탐색)

import sys
input = sys.stdin.readline

N = int(input())    # 입력값 N
result = 0          # N과 비교하기 위한 변수

# 모든 경우의 수 확인
for i in range(1, N+1):
    # i를 문자열로 입력받아 구한 각 자리수를 a리스트에 저장
    a = list(map(int, str(i)))
    # i와 각 자리의 수의 합 더해 분해합 구하기
    s = i + sum(a)

    # 분해합과 N 비교
    if (s == N):
        result = i
        break

print(result)   # 생성자가 없을 경우 0 출력
