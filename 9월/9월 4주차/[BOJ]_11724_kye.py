import queue
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start]) # queue에 맨처음 노드를 넣고
    visited[start] = True  # 방문 처리 True
    while queue: # queue를 다 돌 때까지 while문 반복
        node = queue.popleft() # 맨 왼쪽 노드부터 빠져나간다
        for i in graph[node]: 
            if not visited[i]: # 방문하지 않았다면
                visited[i] = True # 방문처리 하고
                queue.append(i) # 큐에 노드 저장

# 정점 (1<=N<=1000) 간선(0<=M<=NX(N-1)/2)             
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 간선의 양 끝점 u, v (1<u, v<=N, u!=v) 
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].appennd(v)
    graph[v].append(u)
    
# 방문처리
visited = [False] * (1 + N)
count = 0 # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각 돌면서
for i in range(1, N+1):
    if not visited[i]:   # 만약 방문하지 않으면
        if not graph[i]: # 만약 그래프가 비었다면
            count += 1   # 개수 1 추가 
            visited[i] = True # 방문처리
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            bfs(i)  # 해당 i를 시작노드로 bfs를 돈다
            count += 1  # 연결요소를 +1 한다
            
print(count)