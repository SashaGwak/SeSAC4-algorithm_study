# # 막대기
# # 아래 그림처럼 높이만 다르고(같은 높이 막대기 있을 수 있음)

# # 수의 대소 비교해야 됨.
# # 자기 자신, 자기보다 큰 수만 출력한다.

# import sys

# input = sys.stdin.readline 
# # input에 기능 넣어버림. 너무 기니까
# num = int(input())
# a = [] # 막대기 넣을 스택.

# # 보이는 막대기 개수. (자기 자신은 무조건 보이니까)
# longer = 1;

# for i in range(num) :
#     # 막대기 갯수 여러개를 for문 안에서 돌려야 됨.
#     # a1 = int(sys.stdin.readline()) 
#     # a.append(a1);
#     a.append((int(sys.stdin.readline())))
    
# # [] 안에서 대소 비교하는 함수?
# # if 문 돌려서 뭐가 크고 작은지 찾아볼까?

# # 최대값은 스택의 맨 오른쪽
# Max = a[-1]


# # -1은 대체 왜 한거야?
# # (len(a)-1, -1, -1)
# for i in range(len(a), 0, -1) :
# # range(start, stop, step)
#     if a[i] > Max :
#         longer += 1
#         Max = a[i]

import sys

input = int(sys.stdin.readline)
heights = []
N = input()
n = current_h = before_h = 0

for i in range(N) :
	heights.append(input())
for _ in range(N) :
	current_h = heights.pop()

	if current_h > before_h :
		n += 1
		before_h = current_h

print(n)
        




    

