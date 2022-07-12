grade_input = input("성적을 입력해주세요.")
grade = int(grade_input)

if 90 <= grade <= 100 :
    print('A')
elif 80 <= grade <= 89 :
    print('B')
elif 70 <= grade <= 79 :
    print('C')
elif 60 <= grade <= 69 :
    print('D')
else :
    print('F')
