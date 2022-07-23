#2562(최댓값)

N = []
for i in range(9):
    N.append(int(input()))
print(max(N)) # 최댓값
print(N.index(max(N))+1) # 최댓값이 몇 번째 수인지

# list 
#   리스트명 = [요소1, 요소2, 요소3, ...]

# append()
#   리스트의 맨 마지막에 요소 추가하는 함수

# N.index(max(N))+1 이유 
#   리스트는 0부터 시작하기 때문
#   원하는 숫자를 출력하기 위해선 +1를 해야함
