# 1707 이분그래프
# bipartite graph distinction
# 1) dfs
#  정점을 방문하면서 각 정점을 1, -1 그룹으로 분할합니다.
#  이미 방문했던 정점이 현재 정점과 동일한 그룹이면 False를 반환합니다.


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


# dfs
def dfs(start, group):
    visited[start] = group  # 방문한 정점에 해당 그룹으로 설정(1,-1)

    for i in graph[start]:
        if not visited[i]:  # 아직 방문하지 않았다면
            a = dfs(i, -group)  # 그룹값을 -1로 주어(다른 그룹으로 설정) dfs 수행
            if not a:  # 만약 a가 False가 나왔다면
                return False  # False를 리턴
        # 만약 현재 정점과 연결된 정점의 그룹값이 같다면 (방문한 곳이며, 인접한데 같은 그룹이라면)
        elif visited[i] == visited[start]:
            return False  # False를 리턴
    return True  # 그외의 경우는 True를 리턴


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]  # 빈 그래프 생성
    visited = [False] * (V + 1)  # 방문한 정점 체크

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)  # 무방향 그래프
        graph[b].append(a)  # 무방향 그래프

    for i in range(1, V + 1):
        if not visited[i]:  # 아직 방문하지 않았다면, dfs 수행
            result = dfs(i, 1)
            if not result:  # 만약 result가 False가 나왔다면 더이상 수행할 필요가 없으므로
                break  # break

    print("YES" if result else "NO")    # 삼항조건연산자
