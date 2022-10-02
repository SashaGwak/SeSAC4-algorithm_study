import sys
sys.setrecursionlimit(10**6) #재귀 깊이 설정

dx=[-1,0,1,0,-1,-1,1,1] #상하좌우, 대각선
dy=[0,1,0,-1,-1,1,-1,1]

def DFS(i,j):
    for x in range(8): #상하좌우, 대각선
        xx = i + dx[x]
        yy = j + dy[x]
        if 0 <= xx < h and 0 <= yy < w and island_map[xx][yy] == 1:
        #상하좌우 대각선을 살펴보다가 1(육지)가 있으면 0으로 바꾸기
            island_map[xx][yy] = 0 #다시 카운트하지 않으려고
            DFS(xx, yy) #육지가 있으면 그걸 기준으로 또 상하좌우, 대각선 확인하려고



if __name__=='__main__':
    while True:
        w,h=map(int,input().split())
        if w==0 and h==0: break

        #입력받기
        island_map=[]
        for _ in range(h):
            island_map.append(list(map(int,input().split())))

        cnt=0
        for i in range(h):
            for j in range(w): #육지가 발견되면
                if island_map[i][j]==1:
                    cnt+=1 #하나 세고
                    island_map[i][j]=0 #0으로 바꿈. 다시 카운트하지 않으려고
                    DFS(i,j)
        print(cnt)