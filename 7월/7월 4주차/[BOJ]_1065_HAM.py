'''
양의 정수의 각 자리가 등차수열을 이루면 한수라고 함.
등차 수열 : 연속된 두 개의 수의 차이가 일정한 수열.
'''

# 리스트로 받아와서 등차 수열이니까 a1, a2, a3
# 2*a2 = a1+a3 이렇게 계산?
# 이런게 몇개나 있냐 찾기? -> 찾는다기 보다는 for문에 조건 걸어서 세주기.

''' #1 try
a = 110
list(a)
total = 0

if a[1] * 2 == a[0]+ a[2] :
    total += 1
    a += 1

print(total + 99)

# 음 뭔가 잘 안된다.
'''

def han(num):
    cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i)))
        if i < 100 :
            cnt += 1 # 1~99는 모두 한수 
            # 이건 따로 빼는게 좋을 것 같은데, 굳이 if로 99번이나 연산할 필요없어.
        elif num_list[1] * 2 == num_list[0] + num_list[2] :
            cnt += 1
    return cnt

num = int(input())
print(han(num))

# second try ,
# 연산 속도 낮추려고 100이하에서의 한수는 따로 빼서 
# 더해줬는데 뭐 이건 안되는건가? ^~^ 틑렸다고 하네 자꾸. ^~^
# 아 헐 세자리 아니고 한자리, 두자리 수도 포함이라 그랬구나..
# 내가 미안하다.
def han(num):
    cnt = 0
    for i in range(100, num+1):
        num_list = list(map(int,str(i)))
        if num_list[1]*2 == num_list[0]+num_list[2] :
            cnt += 1
    return cnt

num = int(input())
print(han(num)+99)
