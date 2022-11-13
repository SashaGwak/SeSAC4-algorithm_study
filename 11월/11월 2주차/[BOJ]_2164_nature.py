# 2164 카드2

from collections import deque

N = int(input())

# deque - 스택과 큐를 합친 자료구조, 가장자리에 원소를 넣거나 뺄 수 있음
Q = deque(range(1, N+1)) 

while len(Q) != 1: # 카드의 개수가 1개가 될때까지
    # popleft - 덱의 가장 왼쪽에 있는 원소를 덱에서 제거, 그 값을 리턴
    Q.popleft() # 맨 위 카드를 제거
    # append(x) - x를 덱의 오른쪽에 삽입 
    Q.append(Q.popleft()) # 그 다음 오는 카드를 맨 아래 카드에 넣음

print(Q[0]) # 마지막 카드 출력