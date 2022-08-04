# 스택 수열(1874)
import sys
n = int(input())
stack = []

for i in range( n ):
    num = int(sys.stdin.readline())
    stack.append(num)

print(stack)