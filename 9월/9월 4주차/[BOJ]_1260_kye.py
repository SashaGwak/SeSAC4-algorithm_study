import sys 
from collections import deque

# n 값은 문제에서 주어지는 V 값을 넣는 것으로 시작 
# 탐색한 곳은 True 로 값을 바꿈
def dfs (n):
    visited[n] = True
    print(n, end=' ')
    for i in graph[n]: # graph[n]을 통해 n의 값과 연결되어있는 노드로 이동, 다시 dfs 호출
        if not visited[i]:
            dfs(i)
            
def bfs(n):
    queue = deque([n])
    visited[n] = True
    while queue: # queue가 빌 때까지 while문 반복
        v=queue.popleft() # queue의 왼쪽에서 값을 하나 뽑아 출력
        print(v, end=' ') # 방문하지 않은 곳 탐색 -> 방문하지 않았던 노드는 큐에 추가하고 True
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
#정점(1<=N<=1000), 간선(1<=M<10000), 탐색 노드 중 첫번째 노드(V)                
N,M,V = map(int, sys.stdin.readline().split())

# 빈 2차원 배열을 만들고, 방문할 때마다 노드가 들어가고 빠져나갈 것임
graph=[[] for _ in range(N+1)]

# a-b-a-b-a-b 간선을 연결한다
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    # 오름차순으로 정렬
    graph[i].sort()
    
visited = [False] * (N+1) # 방문하지 않은 노드 False

dfs(V)

print()
visited = [False] * (N+1)

bfs(V)
            