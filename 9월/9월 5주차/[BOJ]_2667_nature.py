# 2667 단지번호 붙이기

import sys

input = sys.stdin.readline
N = int(input())

graph = [] # 입력받을 그래프 
result = [] # 결과
count = 0 # dfs 실행마다 연결된 집 수(단지별 집 수)

for i in range(N):
    graph.append(list(map(int, input().rstrip())))

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# dfs 정의
def dfs(x, y):
    global count # global 선언을 해야 전역변수로 사용할 수 있음

    if x < 0 or x >= N or y < 0 or y >= N:
        return
    
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0 # 방문 처리
        for i in range(4): # 상하좌우 방문
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

for i in range(N): # 그래프의 원소가 1일때만 dfs로 방문
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0 # 0으로 초기화


result.sort() # 오름차순

print(len(result)) # 총 단지 수
for i in result: # 각 단지마다 집의 수
    print(i)