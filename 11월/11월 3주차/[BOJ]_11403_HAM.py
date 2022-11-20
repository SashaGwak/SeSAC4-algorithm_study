# BFS
# 각 정점마다 방문했는지 visited에 저장하고, 간선으로 해당 정점이 연결돼 있다면 check에 1을 기록.
# 이 때 visited는 각 정점을 방문하면서 방문 여부 기록.

from collections import deque #  queue 구현을 위한 deque 불러오기.

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)] # 그래프 구현.
# print(graph)  => 출력 시 보이는 화면.
# 3
# 1 1 1 2
# 0 0 1
# 0 1 1
# [[1, 1, 1, 2], [0, 0, 1], [0, 1, 1]] -> print(graph) 출력결과.

visited = [[0]*n for _ in range(n)]   # 2차원 리스트 초기화
# print(visited)
# print([0]*3); # 근데 이게 왜 [0][0][0] 이런 형태가 아니고 [0,0,0]으로 뜰까?
# print(visited) -> 출력 결과 : [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
def bfs(x): # 3입력 시 3번 돌아감. for 문 안에 쓰였으므로.
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]
 
    while queue:
        q = queue.popleft()
 
        for i in range(n):
            if check[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1
 
for i in range(0, n):
    bfs(i)
 
for i in visited:
    print(*i)