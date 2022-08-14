# 펠린드롬수
# 우영우, radar, sees
# 121, 12321
# not 펠린드롬 123,1231, 10 (-> 앞에 무의미한 0은 올 수 없음)

# 입력은 여러 개의 테스트 케이스. 정수 받기
# 입력의 마지막 줄에는 0이 주어짐. (문제에 포함되지 않음)

# 출력 펠린드롬수는 yes 아니면 no

# first try .. 런타임 에러.
# 슬라이싱으로 풀면 되는 문제.
# 근데 뭐가 문젠데..?
import sys
input = sys.stdin.readline
N = int(input())
stack = []

for i in range(N) :
    stack.push(int(input()))

# 이거 어떻게 변환할까?
# 슬라이싱하면 복잡하게 생각안해도 됨.
for i in range(len(stack)) :
    if stack[i] == stack[::-1] :
        print(yes)
    else: 
        print("no")

# second try : 마지막라인에 0이 들어가야 함.
num = input()
while num != 0 :
    if num[::-1] == num :
        print('yes')
    else:
        print("no")
        num = input()

# third try : 왜 자꾸 출력초과라고 뜨는걸까..
# 아 .. while에 break 안걸어줬구나.

while True :
    num = input()
    if num == '0' : 
        break
    elif num == num[::-1] :
        print('yes')
    else :
        print("no")



