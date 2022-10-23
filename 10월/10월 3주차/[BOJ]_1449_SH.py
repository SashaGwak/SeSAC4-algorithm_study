# 1449 수리공 항승 
# 수리할 때 필요한 테이프의 최소 개수
import sys
input = sys.stdin.readline

# 입력값 받기
N, L = map(int, input().split()) # N 물이 새는 곳의 개수, L 테이프의 길이
data = list(map(int, input().split()))  # 물이 새는 곳의 위치 

data.sort()

# 테이프 붙이기 시작 지점
start = data[0]-0.5
end = start + L
count = 1 # 사용 테이프 개수

# 물의 새는 곳의 위치를 받으면서
for i in range(0, len(data)):
  # 테이프를 붙이는 범위 내에 물이 새는 곳의 위치가 있다면
  if start < data[i] < end: 
    # 기존 테이프 사용
    continue
  # 새테이프 사용해야 한다면
  else:
    count += 1
    start = data[i]-0.5
    end = start + L

print(count)