a = []

for i in range(0, 9): #list index의 범위는 9까지이다              
    num = int(input()) #무작위로 숫자를 입력받는다
    a.append(num) #a리스트에 num에서 무작위로 입력받은 숫자를 추가해준다
print(max(a), a.index(max(a))+1, sep = '\n')