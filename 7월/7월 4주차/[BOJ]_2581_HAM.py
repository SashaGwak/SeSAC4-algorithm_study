# 소수 찾기
# m, n사이의 수 중 소수의 합, 가장 작은 소수값 출력.

# for문 돌리면 될 것 같은데?.. 근데... how...?
# 1의 자리 소수 조건 하나씩 달아?(이건 내가 다 아니깐..?) -> 연산 속도 많이 걸리지 않나?
# 10의 자리 소수부터는? 쒯^ㅠ^ (한도 끝도 없이 조건 다는것도 오바다)

# 이중루프문을 좀 더 공부해야 됨.

m = int(input())
n = int(input())

decimal = []

for i in range(m, n+1) :
    count = 0
    for j in range(1, i+1) :
        if i % j == 0 :
            count += 1
            if count > 2 :
                break
    if count == 2 :
        decimal.append(i)
if len(decimal) !=0 :
    print(sum(decimal))
    print(decimal[0])
else :
    print('-1')
        
        


