# 1406 에디터

import sys
input = sys.stdin.readline
l = list(input().rstrip()) 
r = []

for i in range(int(input())):
    command = input().rstrip()
    if command == "L":
        if l:
            r.append(l.pop())
    elif command == "D":
        if r:
            l.append(r.pop())
    elif command == "B":
        if l:
            l.pop()
    else:
        i, x = command.split()
        l.append(x)

l += r[::-1]

print(*l, sep="")

# 참고 : https://my-coding-notes.tistory.com/229

# rstip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거
    # text = ' Water boils at 100 degrees '
    # print('[' + text.rstrip() + ']')
    # [ Water boils at 100 degrees]

# 참고 : https://codechacha.com/ko/python-string-strip/

# *(별표)연산자 : 시퀀스/ 컬렉션을 위치 인수로 압축 해제함
# def sum(a, b, c, d):
    # return a + b + c + d
    # values1 = (1, 2, 3, 4)
    # n = sum(*values1) => n = sum(1, 2, 3, 4)
# 참고 : https://rateye.tistory.com/708

# sep(separation)
    # 구분자
    # print('S', 'E', 'P', sep="") => SEP
# 참고 : https://infinitt.tistory.com/11
