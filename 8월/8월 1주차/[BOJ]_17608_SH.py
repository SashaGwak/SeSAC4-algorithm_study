# 막대기 17608
import sys
N = int(input())
# 높이 넣어줄 리스트 생성
heights = []

for i in range(N):
    val = int(sys.stdin.readline())
    # 높이 리스트 생성
    heights.append(val)

max = heights[-1]

# 보이는 막대기 개수 
# 맨 첫번째 막대기 1개는 항상 보임
count = 1
# 끝 막대기부터 확인
for i in range(-1, -len(heights) - 1 , -1):
# for i in reversed(hegihts) 이런식으로 해줘도 더 간단할 듯 ! 
    # 만약 끝막대기보다 길이 긴 경우 count 1씩 커짐
    if heights[i] > max:
        count += 1
        max = heights[i]

print(count)