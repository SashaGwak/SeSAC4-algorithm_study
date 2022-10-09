# 동전 0 (11047)
import sys
input = sys.stdin.readline
N, K = map(int, input().split())

arr = [ int(input()) for _ in range(N)] 
arr.reverse()
# arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

# 동전 개수
count = 0

for coin in arr: 
    count += K // coin
    K %= coin 

print(count)