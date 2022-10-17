# 19539 사과나무

N = int(input())  # 사과나무 개수
a = list(map(int, input().split()))  # i번째 나무의 희망높이
cnt = 0    # 희망높이가 2 이상인 개수를 담을 변수
flag = True

# 전체 길이 합이 3으로 나눠떨어지는 3의 배수
if sum(a) % 3 == 0:
    for i in range(N):
        cnt += a[i] // 2  # 2 이상인 값의 개수 세기
    if cnt < sum(a) // 3:  # 길이 총합을 3으로 나눈 값과 비교
        flag = False

else:
    flag = False

print('YES') if flag else print('NO')
