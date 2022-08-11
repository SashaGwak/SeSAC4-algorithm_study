# 에디터(1406)
import sys
text = list(sys.stdin.readline())
M = int(input())

for _ in range(M): 
    command = sys.stdin.readline().split()

    if command[0] == 'P' : 
        text.append(command[1])


for t in text:
    if t == '\n': 
        pass
    else:
        print(t, end='')
