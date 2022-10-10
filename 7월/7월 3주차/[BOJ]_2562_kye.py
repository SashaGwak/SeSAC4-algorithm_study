#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고
#최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

num = []

for i in range(0, 9) :
    user_input = int(input("자연수를 입력하세요."))
    num.append(user_input)

print(int(max(num)))
print(num.index(max(num))+1)
