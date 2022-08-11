# 에디터(1406)
import sys
text = list(sys.stdin.readline().strip())
M = int(input())
cursor = len(text)

# 에디터 구현 부분
for _ in range(M): 
    command = sys.stdin.readline().split()

    if command[0] =='L':
        if cursor > 0:
            cursor -= 1 

    if command[0] == 'D':
        if cursor < len(text):
            cursor += 1

    if command[0] == 'P' : 
        text.insert( cursor, command[1])
        cursor += 1

    if command[0] == 'B' : 
        text.pop(cursor)


# 결과 출력 부분
for t in text:
        print(t, end='')
