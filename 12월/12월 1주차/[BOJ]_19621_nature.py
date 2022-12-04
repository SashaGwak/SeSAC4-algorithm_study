# 19621 회의실배정2

N = int(input()) # 회의의 수 
M = []
for _ in range(N) :
    M.append(tuple(map(int, input().split()))) # tuple - list랑 비슷 , but 요소 값의 생성, 삭제, 수정 불가

M.sort()

people = []
lastStart = max([s for s, e, p in M])

def dfs(x, current):
    current += M[x][2]

    if M[x][1] > lastStart:
        people.append(current)
    for i in range(x+1, N):
        if M[x][1] > M[i][0]:
            continue
        dfs(i, current)

for i in range(N):
    dfs(i, 0) 

print(max(people)) 

