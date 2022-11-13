# 2231 분해합 
# 브루트 포스 방법
N = int(input())
result = 0

# 1부터 최대범위까지 모든 경우의 수를 비교
for i in range(1, N + 1): 
    # array 생성 arr [1] ~ arr [1, 0] ~ arr [1, 0 , 0]이런식으로 쭉 올라감
    arr = list(map(int, str(i)))
    # 모든 자리수 더해보기
    s = i + sum(arr)
    # S = N 이면 작은 수부터 올라가므로 가장 작은 생성자를 찾아낸 것, break하고 출력 
    if (s == N): 
        result = i 
        break

print(result)