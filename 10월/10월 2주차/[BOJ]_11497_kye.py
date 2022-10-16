T=int(input()) # T 테이스 케이스

for i in range(T):
    N=int(input()) # N 통나무 개수
    trees=list(map(int,input().split())) # 통나무의 높이를 리스트로 받음
    trees.sort() # 오름차순으로 정렬
    result=0 # result: 난이도
    for j in range(2, N): # 인덱스 차이를 2로 한다. 1 차이나게 두면 가장 끝에 있는 통나무들의 높이차가 커지기 때문.
        result=max(result,abs(trees[j]-trees[j-2])) # abs():절대값  
print(result)