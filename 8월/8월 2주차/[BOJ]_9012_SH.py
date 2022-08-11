# 괄호(9012)
T = int(input())

for _ in range(T):
    stack = []
    a = input()
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack: # 스택에 괄호가 있을 경우 pop
                stack.pop()
            else: #  스택에 괄호가 없을경우 NO(')'만 남아있는 경우)
                print("NO")
                break
    else: # break문으로 끊기지 않고 수행됬을경우 수행한다('('만 남아있는 경우)
        if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
            print("YES")
        else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
            print("NO")
