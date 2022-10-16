from sys import stdin

for i in range(int(stdin.readline())):
    people = []

    for j in range(int(stdin.readline())):
        people.append(list(map(int, stdin.readline().split())))

    people.sort()  # peope = [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]] 서류 등수 정렬
    temp = people[0][1] # temp "면접" 등수를 비교하기 위한 변수. 서류 1등의 면접 등수인 people[0][1] 저장
    cnt = 1

    for j in range(len(people)):
        if temp > people[j][1]: # people[j][1]보다 면접을 더 잘 보면
            cnt += 1            # 합격자 수 +1
            temp = people[j][1] # temp에 방금 합격한 사람의 면접 등수를 저장함 

    print(cnt)