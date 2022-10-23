# 1449 수리공 항승

from sys import stdin

# 입력값 받기
N, L = map(int, stdin.readline().split())
B = list(map(int, stdin.readline().split()))

# 물이 새는 위치 오름차순 정렬
B.sort()

# 테이프를 처음 붙이는 시작지점
start = B[0] - 0.5                  # end = start + L
# 필요한 테이프의 개수
cnt = 1

# 물이 새는 곳의 위치를 차례대로 받으면서
for i in range(1, len(B)):
    # 테이프를 붙이는 범위 내에 물이 새는 곳의 위치가 있다면
    if start + L >= B[i] + 0.5:     # start< arr[i] < end:
        # 기존 테이프 사용
        continue
    # 기존 테이프로 붙이지 못한다면
    else:
        # 새 테이프를 사용하고 테이프 개수 추가
        start = B[i] - 0.5
        cnt += 1

# 필요한 테이프의 개수 출력
print(cnt)
