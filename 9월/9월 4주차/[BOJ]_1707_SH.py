# 이분그래프(1707)
import sys 
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(start, group):
    queue = deque([start])  # 시작 정점 값을 큐에 담는다.
    visited[start] = group  # 시작 정점 그룹을 설정

    while queue: 
        x = queue.popleft()  # 큐의 맨앞 원소를 빼낸다.
        for i in graph[x]:  # 해당 정점에서 갈 수 있는 하위 정점들을 돈다.
            if not visited[i]:  # 만약 그 정점들을 아직 방문하지 않았다면
                queue.append(i)  # 그 정점들을 추가하고
                visited[i] = -1 * visited[x]  # 상위 정점과 다른 그룹으로 편성
            # 만약 정점들을 이미 방문했었는데 같은 그룹이라면
            elif visited[i] == visited[x]:  
                return False  # False를 바로 리턴
    return True  # 위의 조건에 걸리지 않았다면 True를 리턴


# T 테스트 케이스 개수 
T = int(input())

for _ in range(T):
    # V 그래프 정점개수, E 간선 개수
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]  # 빈 그래프 생성
    visited = [False] * (V+1)  # 방문한 정점 체크위한 리스트 
    # 간선 연결
    for _ in range(E): 
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    for i in range(1, V + 1):
        if not visited[i]:  # 방문한 정점이 아니면, bfs 수행
            result = bfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")