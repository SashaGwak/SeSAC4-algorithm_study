from collections import deque
import sys

N, M = map(int, input().split())
visited = [False] *(N+1)
graph = [[] for _ in range(N+1)]


for i in range(M):
    x,y = map(int, sys.stdin.readline().split())
    # 연결돼있는 노드들 담기
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1

print(cnt)