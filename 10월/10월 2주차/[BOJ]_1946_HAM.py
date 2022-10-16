from sys import stdin

for i in range(int(stdin.readline())): # 테스트 케이스 개수 2
    people = [] # people은 리스트로 만들어두고.

    for j in range(int(stdin.readline())):
        people.append(list(map(int, stdin.readline().split())))

    people.sort() 
		# 여기까지 하면 people은
		# [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]
		# 서류 성적으로 1~5등을 정렬해뒀음.
    
    temp = people[0][1] 
		# temp는 면접 등수를 비교하기 위해 만든 변수
		# 서류 1등의 면접 등수인 people[0][1]을 저장해주고,
		# 서류 2등부터 서류 1등보다 면접을 잘 본 사람이 나왔을 때 합격해주면 됨.
		# 대신 합격 처리 이후엔 가장 최근에 합격처리가 된 사람보다 면접을 잘 본 사람을 찾아야 함.

    cnt = 1 # 어떤 경우라도 people[0][1]은 나올 것이므로 cnt=1로 설정

    for j in range(len(people)):
        if temp > people[j][1]: 
            cnt += 1
            temp = people[j][1]
				# temp가 people[j][1]보다 클 때 cnt 변수(합격자 수)에 +1 (면접 점수 올려주기)
    print(cnt)