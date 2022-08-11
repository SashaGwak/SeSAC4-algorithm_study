# 에디터(1406)
import sys

stack_l = list(input().strip())
stack_r = []

for _ in range(int(input())):
    command = sys.stdin.readline().split()

    if command[0] == 'L' and stack_l:
        stack_r.append(stack_l.pop())
    elif command[0] == 'D' and stack_r:
        stack_l.append(stack_r.pop())
    elif command[0] == 'B' and stack_l:
        stack_l.pop()
    elif command[0] == 'P':
        stack_l.append(command[1])

print(''.join(stack_l + list(reversed(stack_r))))
# reversed만 해주면 reversed 객체가 표현된다 -> <list_reverseiterator object at 0x100cdffa0>
