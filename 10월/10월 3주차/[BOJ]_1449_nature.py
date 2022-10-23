# 수리공 항승

# N(물이 새는 곳의 개수), L(테이프의 길이)
# water(물이 새는 곳의 위치)

N, L = map(int, input().split())
water = list(map(int, input().split())) # 물이 새는 곳의 위치
water.sort() # 물이 새는 곳의 위치 정렬

cnt = 0 # 테이프 개수 카운트
tape = 0 # 마지막으로 막은 위치

for i in water:
    if tape < i: # 이미 테이프가 붙어있는 곳은 무시
        cnt += 1
        # 마지막으로 막은 위치 tape 변수에 구멍이 날 때마다 테이프를 붙이고, 
        # 테이프 길이(L) - 여유분의 길이(0.5(왼쪽) + 0.5(오른쪽) = 1))만큼 더해줌 
        tape = i + L - 1 
    else: 
        continue

print(cnt)
