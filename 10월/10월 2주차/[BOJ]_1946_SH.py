# 1946 신입사원 
import sys 
input = sys.stdin.readline

for _ in range(int(input())):  # 테스트 케이스 개수
    people = []

    for j in range(int(input())): # 지원자 수
        people.append(list(map(int, input().split()))) # 지원자 성적 정보

    people.sort() # 서류 성적 기준으로 먼저 정렬
    # people은 [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]

    temp = people[0][1] # 서류 1등의 면접등수 저장 
    cnt = 1

    for j in range(1, len(people)): 
        # 전 사람보다 면접 잘본 사람 나오면 합격
        if temp > people[j][1]: 
            cnt += 1 
            # 가장 최근에 합격처리가 된 사람 저장
            temp = people[j][1]

    print(cnt)