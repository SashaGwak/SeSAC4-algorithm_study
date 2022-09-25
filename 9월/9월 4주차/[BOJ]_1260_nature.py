#1260 DFS와 BFS

from collections import deque

# N -> 정점의 개수
# M -> 간선의 개수
# V -> 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True


dfs_visited = [False] * (N + 1)  # dfs의 방문기록
bfs_visited = [False] * (N + 1)  # bfs의 방문기록

# dfs - 스택과 재귀를 이용
def dfs(V):
    dfs_visited[V] = True  
    print(V, end=" ")
    for i in range(1, N + 1):
        if not dfs_visited[i] and graph[V][i]:  
            dfs(i)  

# bfs - 큐를 이용
def bfs(V):
    queue = deque([V]) 
    bfs_visited[V] = True 
    while queue:  
        popV = queue.popleft()  
        print(popV, end=" ") 
        for i in range(1, N + 1): 
            if not bfs_visited[i] and graph[popV][i]:  
                queue.append(i) 
                bfs_visited[i] = True 

dfs(V)
print()
bfs(V)