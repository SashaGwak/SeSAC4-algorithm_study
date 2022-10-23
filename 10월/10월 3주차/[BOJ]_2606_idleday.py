# 2606 바이러스
# 그래프 탐색 - 연결 요소 찾기 문제

n = int(input())    # 컴퓨터의 수
v = int(input())    # 연결되어있는 컴퓨터 쌍의 수
graph = [[] for i in range(n+1)]  # 연결 경로 저장용 2중 리스트
visited = [0]*(n+1)  # 방문한 컴퓨터 확인용 리스트

# 그래프 생성
for _ in range(v):  # 총 m개의 간선을 입력받아 연결 경로를 graph에 저장
    a, b = map(int, input().split())
    graph[a] += [b]  # a에 b 연결
    graph[b] += [a]  # b에 a 연결 -> 양방향


# dfs - 방문할 컴퓨터 번호를 i로 입력받기
def dfs(v):
    visited[v] = 1  # 1로 방문표시
    # v번 컴퓨터에 연결된 컴퓨터들의 리스트 반복 검사
    for nx in graph(v):
        if visited[nx] == 0:    # 미방문시
            dfs(nx)             # dfs() 재귀호출


# 1번 컴퓨터부터 방문하고 연결된 컴퓨터들을 재귀호출하며 모두 방문
dfs(1)

# 바이러스에 걸린 컴퓨터의 수 출력
print(sum(visited)-1)
