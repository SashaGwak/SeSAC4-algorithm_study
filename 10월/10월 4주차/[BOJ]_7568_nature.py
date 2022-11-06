# 7568 덩치 

N = int(input()) # 전체 사람 수 N

big = [] # 각 사람의 몸무게와 키를 받을 List 

for i in range(N): # 입력한 순서대로 정보를 입력 받음 
    x, y = map(int, input().split())
    big.append((x, y))

for i in big:
    ranking = 1 # 초깃값은 전부 1 
    for j in big:
        if i[0] < j[0] and i[1] < j[1]: # i의 몸무게와 키가 모두 j보다 작다면 
            ranking += 1 # 위 조건 만족 시 count up 
    
    print(ranking)
