# 2667 단지번호붙이기

from collections import deque

n = int(input())

graph = []  # 입력받을 그래프를 담을 리스트 선언
cnt = []    # 결과 리스트 선언

for i in range(n):
    graph.append(list(map(int, input())))


# 한 점 기준으로 상하좌우 한칸씩 이동할 좌표 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    n = len(graph)
    queue = deque()  # 큐 선언
    queue.append((a, b))    # a,b를 큐에서 그대로 빼기위해 append로 추가
    graph[a][b] = 0  # 첫번째 집 a,b 방문처리
    count = 1       # 첫번째 집 방문했기에 count값 1로 시작

    while queue:
        x, y = queue.popleft()  # 큐에 들어간 x,y 빼주기
        for i in range(4):  # 방향별로 이동
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표 이동시, 그래브 범위 벗어나는 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:  # 미방문한 곳이라면
                graph[nx][ny] = 0   # 방문했던 곳 0으로 만들어 재방문 방지
                queue.append((nx, ny))  # 새로운 x,y좌표 큐에 추가
                count += 1  # count값 1 증가
    return count


# 그래프 원소 1일때 bfs로 집 방문
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()  # 오름차순 정렬
print(len(cnt))  # 총 단지수 출력
for i in range(len(cnt)):   # 각 단지마다 집 개수 출력
    print(cnt[i])
