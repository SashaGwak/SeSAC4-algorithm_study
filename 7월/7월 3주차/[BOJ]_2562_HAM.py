# 값을 어떤 형식으로 받을거임? list? 변수값 각각?
# 최대값을 어떻게 찾아내지?  검색 '파이썬 최대값'  
#  max() / list에서 순서 찾는 함수 index()

# first_try
# A = list(input().split())  # 이런 식으로 지정은 안되는건가? (아~~ list로 쓰고 싶으면 list()형태가 아니고 그냥 []로 감싸면 되는거임..)
# print(max(A)) 

# A = [] # 빈 리스트 변수 하나 지정해서 쓰려고 했는데 안되는듯?? 
# A = input().split() # 이게 이상한건가. # list는 split이랑 적용 안됨?
# 아.. split은 문자를 여러개 집어넣어주는 함수니까 문자열을 list형태로 만들어주는 애였구나... 뻘짓했네요...
# print(max(A)) 

A = [int(input()) for _ in range(9)] 
 # 한번에 쓰는 법. [] 리스트 애초에 지정하고, 이 안에서 함수 돌려서 리스트 만들어주기. for와 A.append() 함수를 이용해서 추가해도 됨. 이거 좀 더 공부하셈.
print(max(A))
print(A.index(max(A)) + 1)

