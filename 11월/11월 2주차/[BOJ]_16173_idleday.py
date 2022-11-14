# 16173 점프왕 쩰리
# BFS
# 쩰리 : 맨 왼쪽 위의 칸에서 출발해 (행, 열)로 나타낸 좌표계

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())    # 게임구역의 크기
graph = [list(map(int, input().split()))
         for _ in range(N)]  # 게임판 구역을 입력받는 2차원 리스트
visited = [[False]*3 for _ in range(N)]  # 방문여부 저장용 2차원 리스트

# 방향 벡터 설정
dx = [1, 0]     # 오른쪽만 가능
dy = [0, 1]     # 아래만 가능


def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        # 쩰리가 현재 밟고 있는 칸의 숫자 인출
        step = graph[x][y]

        # 끝점이 -1이므로 -1로 도달하면 성공!
        # x좌표와 y좌표가 N-1에 도달한다면 오른쪽 가장 아래로 이동 가능
        if graph[x][y] == -1:
            return True
        for move in range(2):
            # 쩰리가 현재 밟은 숫자를 인출하고 이동수에 곱해서 이동
            nx = x+dx[move]*step
            ny = y+dy[move]*step

            # 주어진 범위를 벗어나는 경우 무시
            # x,y의 범위가 0,0보다 작아지거나, 주어진 matrix 크기를 초과하는 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 방문하지 않았을 경우
            if not visited[nx][ny]:
                # 방문 처리
                visited[nx][ny] = True
                # 아직 우리가 찾는 조건(graph[x][y] == -1)이 아니므로 q에 담아주고 다시 반복
                q.append([nx, ny])


# 결과 출력
if bfs(0, 0):   # (0,0)에서 출발
    print('HaruHaru')
else:
    print('Hing')
