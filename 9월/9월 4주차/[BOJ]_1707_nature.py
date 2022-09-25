#1707 이분 그래프

import sys
import collections 

# python은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러를 일으킨다.
sys.setrecursionlimit(10**6) # 재귀 최대 깊이 설정
input = sys.stdin.readline

for _ in range(int(input())): # 테스트 케이스의 개수
    # V - 그래프의 정점의 개수, E - 간선의 개수
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)] # 빈 그래프
    visited = [0] * (V + 1) # 방문한 정점 체크

    for _ in range(E):
        x, y = map(int, input().split())
        graph[x].appned(y) # 무방향 그래프
        graph[y].appned(x) # 무방향 그래프

    q = collections.deque() # deque -> 양방향에서 데이터를 처리할 수 있는 queue형 자료구조를 의미
    group = 1
    bipatite = True
    
    #bfs
    for i in range(1, V+1):
        if visited[i] == 0: # 방문 ❌ 정점 bfs 진행
            q.append(i)
            visited[i] = group
            while q:
                v = q.popleft()
                for w in graph[v]:
                    if visited[w] == 0: # 방문 ❌ 
                        q.appned(w) # 큐에 삽입
                        visited[w] = -1 * visited[v] # 현재 노드와 다른 그룹 지정
                    elif visited[v] == visited[w]: # 이미 방문한 경우, 동일한 그룹에 속하면 False
                        bipatite = False

    print('YES' if bipatite else 'NO')