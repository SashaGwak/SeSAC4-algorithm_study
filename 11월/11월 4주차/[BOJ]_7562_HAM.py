from collections import deque 
 
# 나이트의 '이동방향' 미리 입력.
# 해당 리스트는 현재 위치에서 다른 위치로 이동할 위치를 구할 때 사용될 예정. 
dx=[-1,-2,-2,-1,1,2,2,1] # 그림에서 주어진 갈 수 있는 초록색 칸을 표현
dy=[2,1,-1,-2,-2,-1,1,2]
 
n=int(input()) # 테스트 케이스 개수 입력
 
for i in range(n): # 테스트 케이스만큼 반복.
    l=int(input())
    graph=[] # 2차원 리스트로 체스판 구현.
    for i in range(l): 
        graph.append([0]*l) # l*L 체스판이므로 [0]*l만큼의 열을 각 행마다 l번 추가
    queue=deque()
    x,y=map(int,input().split()) # 시작 위치 입력
    w,z=map(int,input().split()) # 목표 위치 입력
    queue.append((x,y)) # 시작 위치를 queue에 넣어주기. # 전에 구조체 만들면서 넣어준거로도 이 방식에 적용할 수 있나?

    # bfs 개념. bfs는 탐색 노드를 큐에 삽입하고 방문처리 후,
    # 큐에서 노드를 꺼내 해당 노트의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하는 것.
    # 따라서 수행할 수 없을 때까지 반복한다는 점에서 queue 내에서 아무 것도 남아있지 않으면 while문을 종료함.
    while queue:
        x,y=queue.popleft() # 가장 처음 입력된 좌표를 꺼낸 후 x,y 현재 위치에 매핑.
        if x==w and y==z: # 이 때 w, z와 비교하여 목표 위치에 도달해있다면 while문 종료. (시간초과 피하는데 중요)
            break # 현재 위치 = 목표위치 같을 떄 while문 종료해야 시간 초과 안뜸. (없으면 그래프의 모든 경우의 수를 구하는 것)
        for i in range(8): # 현재 위치를 기준으로 8방향 구하게 됨.
            nx=x+dx[i] # 따라서 위에서 정해두었던 이동 값을 가져와, 현재값 + 이동값으로 신규 위치를 구함.
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=l or ny>=l: # 신규 위치가 적합한지 검토하는 시간을 가지고 적합하지 않으면 버려야 함.
                continue # 우선 nx의 범위를 정하여 체스판 내 범위에 있는지 확인해야 함.
            if graph[nx][ny]==0: # 한번도 방문하지 않은 곳이라면, 
                graph[nx][ny]=graph[x][y]+1 # 현재 위치까지의 이동 횟수에 이제 신규 좌표로 이동할 것이기 때문에 +1을 더해서 신규 좌표값에 넣어줌.
                queue.append((nx,ny))
    print(graph[w][z]) # 이후 w,z 좌표에서의 값을 print(graph[w][z])로 하여 출력함.