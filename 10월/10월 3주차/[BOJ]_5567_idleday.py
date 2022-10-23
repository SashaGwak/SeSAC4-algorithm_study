# 5567 결혼식
# BFS 그래프 탐색


from collections import deque
import sys
input = sys.stdin.readline


n = int(input())    # 동기의 수
m = int(input())    # 리스트의 길이
visited = [0 for _ in range(n+1)]  # 방문 기록용 배열
graph = [[0]*(n+1) for _ in range(n+1)]  # 친구 저장용 배열

# 친구 관계 저장해놓기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # a와 b
    graph[b].append(a)  # b와 a -> 양방향


def bfs(x):
    q = deque()
    visited[x] = 1
    q.append(x)

    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[a] + 1


bfs(1)
result = 0

for i in range(2, n+1):
    # 본인(1)이거나 친구(2)거나 친구의 친구(3)이면서 방문한 경우
    if visited[i] < 4 and visited[i] != 0:
        result += 1

print(result)
