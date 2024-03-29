from distutils.log import error
import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

def dfs(start, group):
    global error
    
    #만약 사이클이 true라면 재귀탈출
    if error:
        return
    
    visited[start] = group  # 해당 그룹으로 등록
    
    for i in graph[start]:
        if not visited[i]:   # 방문하지 않았다면
            dfs(i, -group)   # 다른 그룹으로 설정
        elif visited[start] == visited[i]:  # 인접한데 같은 그룹이라면 
            error = True   # error값 True
            return  # 재귀 리턴
     
T = int(input())
# 정점의 개수 V, 간선의 개수 E
for _ in range(T):
    V, E = map(int, input().readline())
    graph = [[] for _ in range(V+1)]  # 빈 배열 생성
    visited = [False] * (V + 1) # 방문한 정점 체크
    error = False
    
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append[b]
        graph[b].append[a]
        
    for i in range(1, V+1):
        if not visited[i]:   # 방문하지 않았다면
            dfs(i, 1)  # dfs를 돈다
            if error:  # 만약 에러가 참이면
                break  # 탈출
            
    if error: # 이분 그래프가 아니면 NO
        print('NO')
    else:  # 이분 그래프가 맞으면 YES
        print('YES')