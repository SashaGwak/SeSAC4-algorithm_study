# 바이러스 2606
# 1번 컴퓨터를 통해 웜바이러스에 걸리는 컴퓨터의 수 출력
# 입력값 받기
n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]

# 연결 그래프 생성
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0 
visited = [0]*(n+1)

# dfs 함수 생성
def dfs(start):
    global count
    visited[start] = 1   # 방문 처리 
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i) 
            count += 1

dfs(1)

print(count)