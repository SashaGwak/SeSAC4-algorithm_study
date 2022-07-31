M = int(input())
N = int(input())
S_list = []

for i in range(M, N+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0: # 나눠지면 소수가 아니므로 break
                count += 1
                break
        if count == 0:
            S_list.append(i)

if len(S_list) == 0 : # list에 요소가 없으면 -1 출력   
    print(-1)

else:
    print(sum(S_list))
    print(min(S_list))