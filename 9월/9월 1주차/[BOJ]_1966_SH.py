# 프린터 큐(1966)
import sys
T = int(input())

for _ in range(T):
    # N은 문서의 개수, M 궁긍한 문서 현재 몇번째에 놓여있는지 나타내는 정수(0이 맨왼쪽)
    N, M = map(int, sys.stdin.readline().split())
    # N개 문서의 중요도 차례대로 입력(중요도 같을 수 있음)
    Prioritys = list(map(int, sys.stdin.readline().split()))

    index = [i for i in range(N)]
    index[M] = 'target' # target으로 맞춰서 인덱스 기억하기
    cnt = 0 

    while Prioritys:
        if Prioritys[0] == max(Prioritys): # 중요도가 제일 높다면
            cnt += 1 # 출력 
            if index[0] == 'target': # 우선순위가 가장높고, 우리가 원한 타겟인지 확인
                print(cnt)
                break
            Prioritys.pop(0)
            index.pop(0)
        else:  # 중요도가 가장 높지 않다면
            Prioritys.append(Prioritys.pop(0)) # 우선순위와 인덱스 pop해서 맨뒤로 붙이기
            index.append(index.pop(0))