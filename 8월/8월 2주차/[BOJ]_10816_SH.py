# 숫자 카드 2 (10816)

# 첫번째 답안
# N = int(input())
# numbers = list(map(int, input().split()))
# M = int(input())
# check = list(map(int, input().split()))

# for i in check: 
#     print(numbers.count(i), end=' ')
# -> 시간 초과 뜬 답 
import sys 
input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

numbers.sort()

def bs(num, bound): 
    start, end = 0, n 
    while(start < end): 
        mid = (start + end) // 2 
        # 동일한 수의 가장 낮은 인덱스 찾기
        if bound == 0:
            if numbers[mid] < num:
                start = mid + 1
            else: 
                end = mid
        # 동일한 수의 가장 높은 인덱스 찾기
        else: 
            if numbers[mid] <= num: 
                start = mid + 1
            else: 
                end = mid 
    return end 

result = []
for i in check: 
    # 가장 높은 인덱스에서 가장 낮은 인덱스 빼주기 
    # 예시 문제처럼 i=0 10일때 11-8 = 3
    result.append(bs(i, 1) - bs(i, 0))
print(*result)
