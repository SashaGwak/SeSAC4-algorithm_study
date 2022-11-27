# 11399 ATM

N = int(input()) 
A = list(map(int, input().split()))

A.sort() # 작은 순서대로 정렬
result = 0

for i in range(1, N+1):
    result += sum(A[0:i]) # 리스트의 0번째 수부터 i번째 수까지 더해줌

print(result)
