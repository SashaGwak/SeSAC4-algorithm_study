from collections import deque
 
n = int(input())
queue = deque()
 
for i in range(1,n+1):
    queue.append(i)
 
while True:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    queue.append(queue.popleft())

    # deque는 양방향이 가능