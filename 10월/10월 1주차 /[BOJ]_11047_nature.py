# 11047 동전 0

N, K = map(int, input().split())

moneys = []

for _ in range(N):
    moneys.append(int(input()))

result = 0

for i in reversed(range(N)): # 제일 큰 돈부터 for 문 돌기 위해 
    result += K // moneys[i] # 나온 몫 값을 더하기 
    K %= moneys[i] # 나머지 할당
    if K == 0: # 만약 0이되면 반복문 탈출
        break

print(result)