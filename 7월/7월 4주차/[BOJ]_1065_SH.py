# 한수(1065)
# 문제 
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
# 입력 
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
N = int(input());
hansu = 0

for n in range(1, N + 1):
    # 1부터 99까지는 모두 한수
    if n <= 99:
        hansu += 1
    
    else: 
        # 100부터는 ex) 123 -> 3 - 2 = 2 - 1 -> 한수O
        nums = list(map(int, str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            hansu += 1

print(hansu)