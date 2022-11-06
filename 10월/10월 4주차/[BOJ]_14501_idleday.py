# 14501 퇴사
# dp,brute-force
import sys
input = sys.stdin.readline

N = int(input())    # 퇴사까지 남은 일수
dp = [0]*(N+1)      # 최대수익 저장용 DP 테이블
tplist = []         # t,p 저장 리스트

# 입력값 받기
for _ in range(N):
    t, p = map(int, input.split())
    tplist.append((t, p))
# tplist = [list(map(int, input().split())) for _ in range(N)]


# 최대수익 구하기 (역순)
def consult():
    for day in range(N-1, -1, -1):
        t = tplist[day][0]  # 상담 소요일
        # 해당 일에 근무하는 경우
        if day + t <= N:
            p = tplist[day][1]  # 상담 수입
            # 최대수익 선택
            dp[day] = max(dp[day+1], dp[day+t]+p)
        # 해당 일에 근무하지 않는 경우
        else:
            dp[day] = dp[day+1]


consult()
print(dp[0])


# 최대수익 구하기
for i in range(1, N+1):
    # 상담에 걸리는 날짜 x
    x = tplist[i][0]-1
    # i일의 최대수익은 i-1일과 i일의 최대수익 중 더 큰 값
    dp[i] = max(dp[i-1], dp[i])
    # i일부터 상담완료까지의 최대수익은
    # d[i-1]에 i일에서 Ti일 후 수익을 더한 값과 d[i+x] 중 더 큰 값
    dp[i+x] = max(dp[i-1]+tplist[i][1], dp[i+x])
print(dp[N])
