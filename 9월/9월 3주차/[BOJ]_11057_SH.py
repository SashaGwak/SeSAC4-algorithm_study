# 오르막 수(11057)
# 규칙 num[i] += num [i-1]
n = int(input())

# n = 1일때 지정 
num = [1]*10

for i in range(n-1): # 자릿수
    for j in range(1, 10): # 끝나는 숫자 0-9 
        num[j] += num[j-1]

# 바뀐 num []*10 합 출력 
print(sum(num)%10007)