# 소수(2581)
# 문제 
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
# 입력 
# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.
# 출력
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 
# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
# 소수 -> 1과 자기 자신만으로 나누어떨어지는 함수
M = int(input()) #시작 숫자
N = int(input()) #마지막 숫자

numbers = [] #소수 리스트
for num in range(max(2, M), N + 1): # M이 2 이상부터 시작하도록 조건(1은소수X)
    flag = True
    for i in range(2, num):  #2부터 num-1까지 수로 num 나눠보기
        if num % i == 0:
            flag = False
            break  #2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄(소수 아님)
    if flag: # 똑같은 소수 추가되는 것 막기 위해 추가
        numbers.append(num)  #error가 없으면 소수리스트에 추가

if len(numbers) > 0:
    print(sum(numbers)) 
    print(min(numbers)) 
else:
    print(-1) #소수가 없다면 -1