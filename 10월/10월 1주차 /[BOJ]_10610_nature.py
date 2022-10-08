# 10610 30

N = list(map(str, input()))
N.sort(reverse = True) # 내림차순으로 정렬해서 가장 큰 수를 만들 수 있게 설정
N = "".join(N) # 정렬한 수 합쳐주기

# 30으로 나누어 떨어지면 몫을 출력 
if int(N) % 30 == 0:
    print(N)

# 아니면 -1 출력
else :
    print(-1) 