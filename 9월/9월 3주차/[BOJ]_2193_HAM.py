import sys
n = int(sys.stdin.readline())

dp = [0]*91 # 90까지 개수 세어야 하므로 91개 받음


for i in range(1, n+1) :
	if i == 1 :
		dp[i] = 1 # 1이면 경우의 수 1
	elif i == 2 :
		dp[i] = 1 # 2이면 경우의 수 1
	else :
		dp[i] = dp[i-1] + dp[i-2] # 점화식

print(dp[n])