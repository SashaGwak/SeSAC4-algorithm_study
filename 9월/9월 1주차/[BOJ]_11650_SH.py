# 좌표 정렬하기(11650)
import sys
input = sys.stdin.readline

n = int(input())

# 좌표 모두 들어갈 리스트 만들기 
array = []

# 좌표 넣어주기 
for i in range(n): 
    [a, b] = map(int, input().split())
    array.append([a, b]) 

# 정렬 
s_array = sorted(array)

for i in range(n): 
    print(s_array[i][0], s_array[i][1])