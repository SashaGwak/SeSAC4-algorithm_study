# 16974 레벨 햄버거

import sys
input = sys.stdin.readline

# N: 햄버거 레벨, X: 먹은 재료 수
N, X = map(int, input().split())

burger = [1] * 51       # 버거의 총 재료 수
patty = [1] * 51        # 버거의 총 패티 수

# i번째 햄버거의 전체 재료수와 패티수 각각 저장
for i in range(1, N+1):
    burger[i] = 1 + burger[i - 1] + 1 + burger[i - 1] + 1
    patty[i] = patty[i - 1] + 1 + patty[i - 1]


# 먹은 패티 개수 구하기
def getPatty(N, X):

    if N == 0:                          # 레벨0 (패티 한 장인 경우)
        return X

    if X == 1:                          # 마지막 재료인 햄버거 번만 먹은 경우
        return 0
    elif X <= 1 + burger[N - 1]:                        # case 1
        return getPatty(N - 1, X - 1)                       # 맨 아래 번 빼고 X-1
    # case 2  (딱 가운데 패티까지 먹은 경우)
    elif X == 1 + burger[N - 1] + 1:
        return patty[N - 1]+1
    elif X <= 1 + burger[N - 1] + 1 + burger[N - 1]:    # case 3
        return patty[N - 1] + 1 + getPatty(N - 1, X - burger[N - 1] - 2)
    else:                                               # case4 (버거 다 먹은 경우)
        return patty[N]


print(getPatty(N, X))
