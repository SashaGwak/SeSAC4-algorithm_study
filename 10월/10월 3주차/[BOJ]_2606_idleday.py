# 2606 바이러스
# 그래프 탐색 - 연결 요소 찾기 문제

n = int(input())    # 컴퓨터의 수
m = int(input())    # 연결되어있는 컴퓨터 쌍의 수

graph = [[] for _ in range(n+1)]  # 연결경로 저장용 2중 리스트


# 그래프 생성
for _ in range(m):  # 총 m개의 간선을 입력받아 연결경로를 graph에 저장
    a, b = map(int, input().split())
    graph[a].append(b)  # a에 b 연결
    graph[b].append(a)  # b에 a 연결 -> 양방향

visited = [0] * (n+1)   # 방문한 컴퓨터 확인용 리스트


def dfs(graph, v, visited):  # 방문할 컴퓨터 번호를 v로 입력받기
    visited[v] = 1          # 1로 방문표시
    # v번 컴퓨터에 연결된 컴퓨터들의 리스트 반복 검사
    for i in graph[v]:
        if visited[i] == 0:  # 미방문시
            dfs(graph, i, visited)  # dfs() 재귀호출


# 1번 컴퓨터부터 방문하고 연결된 컴퓨터들을 재귀호출하며 모두 방문
dfs(graph, 1, visited)

# 바이러스에 걸린 컴퓨터의 수 출력
print(sum(visited)-1)   # DFS를 시작할 때 visit[v] = 1을 했기 때문에 -1 해준다.
