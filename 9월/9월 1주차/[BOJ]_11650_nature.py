# 11650 좌표 정렬하기

import sys

input = sys.stdin.readline

N = int(input())
list = []
for i in range(N) :
    x, y = map(int, input().split())
    list.append((x, y))

for i in sorted(list) :
    print(i[0], i[1])

# sorted(정렬할 데이터)
# sorted 함수 - 파이썬 내장 함수
# iterable 한 데이터를 새로운 정렬된 리스트로 만들어서 반환해줌
