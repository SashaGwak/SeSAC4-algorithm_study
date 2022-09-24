# DFS와 BFS(1260)
import sys 
from collections import deque
input = sys.stdin.readline

def dfs(n):
    # 현재 노드 방문 처리 
    visited[n] = True
    print(n, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문 
    for i in graph[n]:
        # 방문처리 되었는지 확인
        if not visited[i]: 
            dfs(i)

def bfs(n): 
    # 큐 생성
    queue = deque([n])
    visited[n] = True
    # 큐가 빌때까지 반복
    while queue: 
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]: 
                queue.append(i)
                visited[i] = True
                

N, M, V = map(int, input().split())
# N 정점의 개수(1 ≤ N ≤ 1,000), M는 간선의 개수 M(1 ≤ M ≤ 10,000) ,V는 탐색을 시작할 정점의 번호 

graph = [[] for _ in range(N+1)]
# 빈 2차원 배열 생성

# 간선을 연결하는 두 정점의 번호가 주어짐 
# 1 2 이면, 1-2 연결이니까 1노드와 연결된 번호에 2 들어감
for i in range(M): 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()
'''
입력값 
4 5 1
1 2
1 3
1 4
2 4
3 4
일때, 그래프 [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
'''

visited = [False] * (N+1)

dfs(V)
print()

visited = [False] * (N+1)

bfs(V)