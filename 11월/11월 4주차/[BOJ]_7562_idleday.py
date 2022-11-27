# 7562 나이트의 이동
# BFS

from collections import deque
import sys
input = sys.stdin.readline

# 나이트가 이동할 수 있는 8가지 방향 정의
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


# BFS 탐색
def bfs(x, y):

    # 시작점 큐에 넣기
    q = deque([[x, y]])

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 뽑은 원소의 위치 정보
        x, y = q.popleft()

        # 도착점에 도착하면
        if x == a and y == b:
            return visited[x][y]

        # 8방향 탐색
        for i in range(8):
            # 이동할 위치
            nx, ny = x+dx[i], y+dy[i]

            # 이동할 위치가 범위 안에 있고, 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 이동 횟수 1 증가
                visited[nx][ny] = visited[x][y]+1
                # 이동할 위치를 큐에 삽입
                q.append([nx, ny])


# 테스트 케이스 개수 입력
t = int(input())

# 테스트 케이스 개수만큼 반복
for _ in range(t):
    n = int(input())    # 체스판 한 변의 길이 입력
    visited = [[0]*n for _ in range(n)]  # 방문 여부 확인용 2차원 리스트
    x, y = map(int, input().split())  # 시작점 입력
    a, b = map(int, input().split())  # 도착점 입력

    # 나이트가 이동하려는 위치까지의 최소 이동 횟수 출력
    print(bfs(x, y))
