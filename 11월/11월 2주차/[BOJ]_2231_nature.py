# 2231 분해합

N = int(input())
result = 0

for i in range(1, N+1): # 1부터 N까지 
    D = list(map(int, str(i))) # 입력값의 각 자리 수 분해
    S = i + sum(D) # 분해합을 구함

    if (S == N): # 만약 분해합이 입력값과 같다면 
        result = i # result = i
        break

print(result)