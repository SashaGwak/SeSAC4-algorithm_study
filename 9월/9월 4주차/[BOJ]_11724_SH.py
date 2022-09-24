# 연결 요소의 개수(11724)
from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue: 
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]: 
                queue.append(i)
                visited[i] = True

# N 정점의 개수, M 간선의 개수
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M): 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1): 
    graph[i].sort()
'''
6 5
1 2
2 5
5 1
3 4
4 6
일 경우, 그래프 [[], [2, 5], [1, 5], [4], [3, 6], [1, 2], [4]]
'''

cnt = 0 
for i in range(1, N+1): 
    if not visited[i]: 
        # bfs가 실행될때마다 cnt +1(연결요소 개수 구해줌)
        bfs(graph, i, visited)
        cnt += 1 

print(cnt)