# 2606 바이러스 

# 첫째 줄 : 컴퓨터의 수 (100 이하, 1번 부터 차례대로 번호가 매겨짐)
# 둘째 줄 : 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어짐 
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어짐

C = int(input()) # 컴퓨터의 수 
N = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수 

graph = [[] for i in range(C+1)] # 그래프 초기화
visited = [0] * (C+1) # 방문한 컴퓨터인지 표시 

for i in range(N): # 그래프 생성 
    x, y = map(int, input().split())
    graph[x] += [y] # x에 y를 연결 
    graph[y] += [x] # y에 x를 연결 

def dfs(N): # 방문할 컴퓨터 번호를 N으로 입력받음 
    visited[N] = 1 # 방문 표시 
    for next in graph[N]: # graph[N]: N번 컴퓨터에 연결된 컴퓨터들의 리스트, 각 컴퓨터를 next로 반복 
        if visited[next] == 0: # 해당 컴퓨터가 방문되지 않은 컴퓨터인지 검사
            dfs(next) # 방문되지 않았따면, dfs(next) 재귀 호출을 통해 해당 컴퓨터를 방문하고 이 과정을 반복 

dfs(1) # 1번 컴퓨터부터 방문
print(sum(visited) - 1) # 1번 컴퓨터를 제외하고, 1번 컴퓨터와 연결된 컴퓨터 개수를 출력