#문제: N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
#입력: 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
#출력: 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

num = int(input())

a = 0
for i in range(1, num+1):
    num_list = list(map(int, str(i)))
    if i < 100:   #한자릿수, 두자릿수는 한수에 포함된다. 비교대상이 없기 때문에. 
        a += 1
    elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
        a += 1
print(a)
