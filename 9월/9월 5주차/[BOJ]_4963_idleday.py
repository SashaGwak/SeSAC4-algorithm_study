# 4963 섬의 개수

from collections import deque
import sys
sys.stdin.readline()
sys.setrecursionlimit(1000000)  # 재귀제한조건


# 상하좌우
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# 대각선
# dx = [-1, -1, 1, 1]
# dy = [-1, 1, -1, 1]

# 상하좌우 + 대각선 방향까지 인접그룹
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


# bfs
def bfs(i, j):  # 방문시작 좌표
    s[i][j] = 0
    queue = [[i, j]]  # 매개변수의 좌표 삽입
    # q = deque()  q.append([x, y])도 가능

    while queue:
        a, b = queue[0][0], queue[0][1]  # a,b = queue.popleft()
        del queue[0]

        for k in range(8):  # 8방향 조사
            x = a + dx[k]
            y = b + dy[k]

# 방문할 수 있고(지도 벗어나지않았고), 섬(1)인 경우에만 방문처리 & 큐에 해당 좌표 삽입
            if 0 <= x < h and 0 <= y < w and s[x][y] == 1:
                s[x][y] = 0
                queue.append([x, y])


while True:
    # user input
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    # init
    s = []
    cnt = 0

    for _ in range(h):
        s.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if s[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
