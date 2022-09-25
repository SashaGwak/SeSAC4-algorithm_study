# 이분그래프(1707)
from collections import deque
import sys 
input = sys.stdin.readline

def dfs(start, group):
    visited[start] = group # 해당 정점의 group 설정(1,-1)

    for i in graph[start]:
        if not visited[i]: # 만약 방문하지 않았다면
            a = dfs(i, -group) # 그룹값을 -1로 주어 dfs를 돈다.
            if not a: # 만약 a가 false가 나왔다면
                return False 
            elif visited[i] == visited[start]:  # 만약 현재 정점과 연결된 정점의 그룹값이 같다면
                 return False  # False를 리턴
    return True  # 그외의 경우는 True를 리턴



# T 테스트 케이스 개수 
T = int(input())

for _ in range(T):
    # V 그래프 정점개수, E 간선 개수
    V, E = map(int, input().split())
    graph = [[] * (V+1)]  # 빈 그래프 생성
    visited = [False] * (V+1)  # 방문한 정점 체크위한 리스트 
    # 간선 연결
    for _ in range(E): 
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    for i in range(1, V+1): 
        if not visited[i]:  # 방문한 정점이 아니면, dfs 수행
            result = dfs(i, 1)
            if not result:  # 만약 result가 False가 나왔다면 더이상 수행할 필요가 없으므로
                break 

print("YES" if result else "NO")