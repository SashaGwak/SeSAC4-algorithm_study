# 통나무 건너뛰기(11497)
import sys 
input = sys.stdin.readline

def tongnamu(l):
    result = 0

    # 정렬한 상태에서 짝수번째 애들을 맨뒤로 보내준다고 생각
    for i in range(len(l) - 2):
        # 따라서 2칸씩 띄워서 차이를 구하고 그 가장 큰 값을 결과값으로 보내줌
        if l[i+2]-l[i] > result: 
            result = l[i+2] - l[i]

    return result 

T = int(input()) 

for _ in range(T): 
    N = int(input())
    List = list(map(int, input().split()))
    print(tongnamu(sorted(List))) # 먼저 정렬을 수행
