# 7568 덩치 (silver5)
# 본인보다 크고 무거운 사람이 몇명인지 찾아서 본인 등수 정하면 됨.

num_student = int(input()) # 전체 사람 수
student_list = [] # 학생들 몸무게-키 넣을 list

for _ in range(num_student): # 전체 수만큼 반복문
    weight, height = map(int, input().split()) # 공백으로 구분해서 입력
    student_list.append((weight, height)) # list에 받은 값 넣어주기.

for i in student_list: # 학생 수만큼 반복문
    rank = 1 
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")