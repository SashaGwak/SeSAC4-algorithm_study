# 16173 점프왕 쩰리

import sys
from collections import deque


def solution(N, graph):
    visited = [[False] * N for _ in range(N)]

    dx = [1, 0]
    dy = [0, 1]

    def dfs(x, y, visited):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            if graph[x][y] == -1:
                return 'HaruHaru'

            jump = graph[x][y]  # 점프 값
            for i in range(2):
                nx = x + dx[i] * jump
                ny = y + dy[i] * jump

                if nx >= N or ny >= N:
                    continue
                if visited[nx][ny]:
                    continue
                else:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        return 'Hing'

    print(dfs(0, 0, visited))


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    solution(N, graph)