x = int(input()) # 첫째 줄에 수열 A의 크기 입력
arr = list(map(int, input().split())) # 둘째 줄에 수열 A를 이루는 A 입력

dp = [1 for i in range(x)] 
# dp[i]의 값을 1로 초기화. x개 만들었음.
# 1로 초기화 한 이유 : 어떠한 경우라도 수열크기는 1 이상이므로.

# 이중 for문
for i in range(x) : # 수열의 크기만큼 for문 돌리고, for문 이해가 안되면 예시를 넣어서 생각.
	for j in range(i) : 
		if arr[i] > arr[j]
				dp[i] = max(dp[i], dp[j]+1) # dp 내 각 원소가 가질 수 있는 수열의 최대크기를 저장.
				
print(max(dp)) # dp배열 원소 중 가장 큰 원소 출력