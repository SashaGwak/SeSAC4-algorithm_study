# 1822 차집합
# 해시맵 자료구조

# 각 집합의 원소의 개수 입력
nA, nB = map(int, input().split()) 

# set() 자료구조에 각 집합 입력
A = set(map(int, input().split())) 
B = set(map(int, input().split())) 


# 차집합 연산
res = []   
for n in A:
    if n not in B:
        res.append(n) 
# res = A-B   

res.sort()          # 정렬시 list로 변환
print(len(res))     # 차집합 길이 출력

if len(res) !=0: 
    print(*(res))   # 차집합 원소 출력