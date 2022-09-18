n = int(input()) # 수의 길이 입력

dp = [[0]*10 for _ in range(n+1)]
	# dp 초기화
	# dp[i][j]에서 i는 자리수, j는 끝에 오는 수
	
dp[1] = [1]*10
# 자릿수가 1일 때, 맨 뒷자리 수(0~9)에 따른 경우의 수

for i in range(1, n+1) : # n의 입력값(자리수)이 1부터 1000까지
	for j in range(0, 10): # 끝에 오는 수는 0~9까지
		for k in range(0, j+1): # 점화식으로 dp에 값 넣기
			dp[i][j] += dp[i-1][k] # 점화식

print(sum(dp[n])%10007)