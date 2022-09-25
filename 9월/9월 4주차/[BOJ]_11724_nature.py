#11724 연결 요소의 개수

import sys

# python은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러를 일으킨다.
sys.setrecursionlimit(10**6) # 재귀 최대 깊이 설정
input = sys.stdin.readline

# N -> 정점의 개수 
# M -> 간선의 개수
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)] # graph 리스트 초기화
visited = [False] * (N + 1) # 방문기록 초기화
cnt = 0 # 출력 숫자 카운트

# u, v -> M개의 줄에 주어진 간선의 양 끝점
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        cnt += 1

print(cnt)