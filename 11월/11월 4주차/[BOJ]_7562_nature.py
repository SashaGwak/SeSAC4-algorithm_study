# 7562 나이트의 이동

from collections import deque
import sys

input = sys.stdin.readline
T = int(input().rstrip())

def bfs() :
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    q = deque()
    q.append((startX, startY))
    while q :
        x, y = q.popleft()
        if x == endX and y == endY :
            return matrix[x][y] -1 
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<L and 0<=ny<L and matrix[nx][ny] == 0 :
                matrix[nx][ny] = matrix[x][y] + 1
                q.append((nx,ny))
                
for _ in range(T) :
    L = int(input().rstrip())
    startX, startY = map(int, input().rstrip().split())
    endX, endY = map(int, input().rstrip().split())
    matrix = [[0]*L for _ in range(L)]
    matrix[startX][startY] = 1
    print(bfs())