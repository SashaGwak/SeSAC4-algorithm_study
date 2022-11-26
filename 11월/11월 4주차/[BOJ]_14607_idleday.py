# 14606 피자 (Small)
# Dynamic Programming

N = int(input())
dp = [0]*(11)   # N 개수에 따른 즐거움 값 저장

# 기저사례 처리
dp[1] = 0
dp[2] = 1

# N=3부터 현재 개수까지 순차적으로 즐거움 값 계산
for i in range(3, N+1):
    #  즐거움의 총합은 N을 반으로 나누었을 때가 가장 크다
    m = i//2    # N을 반으로 나눈 값
    # 점화식 세우기
    dp[i] = m*(i-m) + dp[m] + dp[i-m]    # 즐거움 값 + 절반1 + 절반2
print(dp[N])


# 14607 피자 (Large)
# 수학
# 1 ≤ N ≤ 10^9 이기 때문에 O(n)의 시간 복잡도를 가진 DP 쓰면 시간 초과

N = int(input())
print((N*(N-1)) // 2)   # 정수로 출력하기 위해 //사용
