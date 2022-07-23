#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고
#최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다.
#주어지는 자연수는 100 보다 작다.

num = []

for i in range(0, 9) :
    user_input = int(input("자연수를 입력하세요."))
    num.append(user_input)

print(int(max(num)))
    
