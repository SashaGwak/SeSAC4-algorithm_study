# [7월 2주차] Python Summary
내장함수에 대해 공부했다.

## **split 함수**
- 기본형: 문자열.split([sep], [maxsplit])
- 문자열을 maxsplit 횟수만큼 sep의 구분자를 기준으로 문자열을 잘라서 리스트로 만든다. \
- **sep 파라미터**: 문자열을 나누는 기호를 값으로 입력한다. 기본값은 none이고 공백(띄어쓰기, 탭 등)을 기준으로 문자열을 나눈다.
- **maxsplit 파라미터**: 문자를 나눌 최대 분할 수. 기본값은 -1이고 제한 없음을 의미한다. 아무 값도 넣지 않으면 문자 전체를 나눈다.
	```python
	#예시
	문자열.split(1)            #불가능
	문자열.split(',', 1)       #가능
	문자열.split(maxsplit=1)   #가능

	test = 'Hello world : 헬로 월드'
	print(test)
	print(test.split()) // 공백 기준으로 나눈다.
	print(test.split(sep=':')) // : 기준으로 나눈다.
	print(test.split(maxsplit=1)) // 공백 기준 한 번 분할한다. 
	print(test.split(maxsplit=2)) // 공백 기준 두 번 분할한다.
	print(test.split(maxsplit=3)) // 공백 기준 세 번 분할한다.

	#result:
	Hello world : 헬로 월드
	['Hello', 'world', ':', '헬로', '월드']
	['Hello world ', ' 헬로 월드']
	['Hello', 'world : 헬로 월드']
	['Hello', 'world', ': 헬로 월드']
	['Hello', 'world', ':', '헬로 월드']
	```

## **input 함수**
사용자의 입력값을 **문자열**로 받는다.
+ 숫자열로 바꾸고 싶을 때: 정수형 int(), 실수형 float()

## **map 함수**
- 기본형: map(function, iterable) *iterable: 반복 가능한 자료형(ex. list, dict, range, tuple, etc.)
- 두 번째 인자로 들어온 반복가능한 자료형을 첫 번째 인자로 들어온 함수에 하나씩 집어넣은 다음 함수가 수행한 결과를 묶어서 돌려준다.
	```python
	#예시
	def two_times(numberList):             # numberList 매개변수를 받는 two_times 함수 선언
		result = [ ]                       # result 값이 비어있는 상태
		for number in numberList:          # number는 numberList의 각각의 요소로 지정된다.  
			result.append(number*2)        # number*2 값이 result로 들어간다. 
		return result                      # result 값으로 반환한다.  

	result = two_times([1, 2, 3, 4])
	print(result)                          # 결과값: [2, 4, 6, 8]

	#위 예제를 map 함수로 바꿔보자.

	def two_times(x):
		return x*2

	list(map(two_times, [1, 2, 3, 4]))
	[2, 4, 6, 8]
	```

## **print()**
- **sep 파라미터(separation)**
	-기본형: print(문자열, 문자열…,  sep=”구분자”)
	-쉼표로 구분된 각각의 출력값 사이에 구분자를 삽입한다.  기본값은 공백
- **end 파라미터**
	-기본형: print(문자열, 문자열…, end=”구분자”)
	-문장의 끝에 내용을 삽입한다.
	-줄바꿈을 하지 않는다.
	```python
	#예시
	print("010","1234","5658", sep="-")
	print("010","1234","5658", end="-")
	print("홍길동")
	print("Hello",end=" ")
	print("World!")

	#result:
	010-1234-5658
	010 1234 5658-홍길동
	Hello World!
	```

## 문자열 만들기
```python
1. 큰 따옴표(”)로 양쪽 둘러싸기 
"Hello World"
2. 작은 따옴표(’)로 양쪽 둘러싸기 
'Hello World'
3. 큰 따옴표 3개를 연속(”””)으로 써서 양쪽 둘러싸기
"""Life is too short, You need python"""
4. 작은 따옴표 3개를 연속(’’’)으로 써서 양쪽 둘러싸기 
'''Life is too short, You need python'''

#문자 중간에 작은따옴표나 큰따옴표 포함 시킬 때
python = "Hello, I'm Python"

#백슬리시(\)를 사용해서 작음따옴표(')와 큰따옴포(")를 문자열에 포함 시킬 때
python = "Hello, I\'m Python"                 # Hello, I'm Python
say = "\"Python is very easy.\" she says."    # "Python is very easy." she says.
```

## **Escape**
| 문자 | 설명 |
|:---|:---:|
| \n | 줄바꿈 |
| \t | 탭 |
| \b | 백스페이스 |
| \000 | 널문자 |
| \\ | \ |
| \’ | 작은따옴표 |
| \” | 큰따옴표 |

## **if-elif-else 조건문**
```python
if 조건:
	출력할 내용
elif 조건:
	출력할 내용
elif 조건:
	출력할 내용
else:
	출력할 내용
```
if - elif - else 의 순서에 주의한다.
파이썬은 tab에 민감하므로 들여쓰는 부분을 잘 살펴야 한다.