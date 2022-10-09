# 1783 병든나이트
N, M = map(int, input().split())
# 세로가 1이면 시작지점만 방문 가능
if N == 1: 
    print(1)
# 세로가 2라면 2, 3번 방법만 쓸 수 있으므로 
elif N == 2: 
    print(min(4, (M + 1) // 2))
# 세로가 3이상일때
else: 
    # 가로가 6 이하라면 모든 방법을 쓸 수 가 없음(1, 4번 방법을 이용하는게 최대값)
    if M <= 6:
        print(min(4, M))
    # 모든 방법을 쓸 수 있음
    else:
        print(M - 2)
