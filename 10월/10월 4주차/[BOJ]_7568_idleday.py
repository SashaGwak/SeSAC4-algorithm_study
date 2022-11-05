# 7568 덩치
# 완전탐색(Brute-Force Search)

num_student = int(input())  # 모든 사람의 수
student_list = []   # 각 사람의 몸무게와 키를 담을 리스트

for _ in range(num_student):
    weight, height = map(int, input().split())
    # 몸무게와 키를 튜플로 리스트에 삽입
    student_list.append((weight, height))

for i in student_list:  #
    rank = 1            #
    for j in student_list:              #
        if i[0] < j[0] and i[1] < j[1]:  # 몸무게와 키 모두 더 큰 사람이 있는 경우
            rank += 1                   # 덩치 등수 더해서 자기 등수 정하기
    print(rank, end=" ")
