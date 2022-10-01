# 단지번호 붙이기(2267)
N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(x,y):
    if x<0 or x>=N or y<0 or y >=N:
        return False
    
    if graph[x][y] == 1:
        global count
        count += 1  # 단지 수 몇개인지 체크
        graph[x][y] = 0   # 이후 방문하지 않도록 처리
        for i in range(4):   # 상하좌우 체크
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx,ny)
        return True
    return False
    
num = [] # 아파트 단지별 숫자
count = 0 # 아파트 단지 세기 위한 
result = 0 # 총 단지수 

for i in range(N):
    for j in range(N): 
        if DFS(i,j) == True:
            num.append(count)
            result += 1
            count = 0


num.sort() # 오름차순
print(result)
for i in range(len(num)):
	print(num[i])