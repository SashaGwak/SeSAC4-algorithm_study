import sys

lstack = list(sys.stdin.readline().strip())
rstack = []

N = int(input())

for _ in range(N):
    cmd = sys.stdin.readline()
    if cmd[0] == 'L':
        if lstack:
            rstack.append(lstack.pop())
    elif cmd[0] == 'D':
        if rstack:
            lstack.append(rstack.pop())
    elif cmd[0] == 'B':
        if lstack:
            lstack.pop()
    else:
        lstack.append(cmd[2])

print(''.join(lstack + rstack[::-1]))
