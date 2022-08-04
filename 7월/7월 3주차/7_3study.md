# [7월 3주차] Python Summary

## list.index()
- list.index(sub [,start [,end]]) : index(찾을 문자열, 시작점, 종료점)
- index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.
    - 찾고자하는 값이 문자나 문자열인 경우 대소문자를 구분한다!
    - 값이 존재하지 않으면 ValueError를 반환
- 문자열, 리스트, 튜플 자료형에서 사용 가능. 제외)딕셔너리 자료형

```python
a = [1,2,3]
a.index(3) # 2 : 숫자 3의 인덱스 위치가 2
a.index(1) # 0 : 숫자 1의 인덱스 위치가 1

'abcdefghijk'.index('f') # 5 : 문자열 중 f를 찾아
'abcdefghijk'.index('e', 2) # 4 : 문자열에서 2번째 시작점부터 e를 찾아
'abcdefghijk'.index('c', 5, 7) # ValueError: substring not found : 문자열에서 5번째 시작점부터 7번째 종료점 안에서 c를 찾아
```

## list.count()
- list.count(value)
- list에서 찾고자 하는 값의 개수를 반환
    - 찾고자 하는 값이 존재하지 않으면 0을 반환
- 문자열, 튜플, 리스트 사용 가능. 제외) 딕셔너리, 세트 자료형

```python
#예시1
a = 'icecream'
a.count('c') # 2
a.count('x') # 0

#예시2
list = ['apple', 'melon', 'grape', 'kiwi']
count = list.count('apple')
print(count)
# print: 1

#불리언 타입을 튜플 타입으로 변환해서 count 함수 사용하기 <
bool = True, False, True
bool.count(True) # 2
type(bool) # <class 'tuple'>
```

## list.append()
- list.append(value)
- 리스트의 맨 마지막에 입력값 추가

```python
colors = [ red, yellow, green ]
colors.append(orange)
colors # [ red, yellow, green, orange]
```
참고 : [https://wikidocs.net/14](https://wikidocs.net/14)

### list.map()
- .map(function, iterable) → map(적용시킬 함수, 적용할 값)
    - 첫 번째 매개변수로 함수가 오고, 두 번째 매개변수로는 반복 가능한 자료형(리스트, 튜플 등)이 옴.
    - map 함수의 반환 값은 map객체이기 떄문에 해당 자료형을 list 혹은 tuple로 형 변환 시켜줘야 함
    - 함수의 동작: 두 번째 인자로 들어온 반복 가능한 자료형(리스트나 튜플)을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행.
         EX) 첫 번째 인자가 값에 +1을 해주는 함수라고 하면, 두 번째 인자에 [1,2,3,4,5]라는 리스트를 집어넣게 된다면
    - map (값에 +1해주는 함수, [1,2,3,4,5])
        - 함수의 반환을 list(. )로 감싸주면 [2,3,4,5,6]이 되는 함수.

## find()
- .find(sub [,start [,end]]) : find(찾을 문자열, 시작점, 종료점)
- 찾을 문자 혹은 찾을 문자열이 존재하는 지 확인하고
    - 찾는 문자가 존재한다면 해당 위치의 index를 반환하고
    - 찾는 문자가 존재하지 않는다면 -1을 반환
    - 만약 찾는 문자나 문자열이 여러개 있다면 맨 처음 찾은 문자의 index를 반환
    -문자열을 찾을 수 있는 변수는 문자열만 사용이 가능하다. 제외) 리스트, 튜플, 딕셔너리 자료형

```python
#예시1
word = 'saturday'
word.find('f') # -1
word.find('s') # 0
word.find('a') # 1 : 첫번째 a의 위치만 출력한다.

#예시2
str = 'abcabcabc'
index = str.find('b') # index는1 (2번째 문자)
```

## str()
- 숫자형을 문자형으로 바꾸는 함수
- str(숫자)

```python
str(396)  # '396'
str(5.52) # '5.52'
str('hi') # 'hi'
str('hi'.upper()) # 'HI'
```

## 문자열 포맷 코드
변수를 문자열과 함께 출력할 때 사용한다.

| 코드 | 설명 |
| --- | --- |
| %s | 문자열(String) |
| %c | 문자 1개(character) |
| %d | 정수(Integer) |
| %f | 부동소수(floating-point) |
| %o | 8진수 |
| %x | 16진수 |
| %% | Literal % (문자 % 자체) |

```python
name = 'Amy'
>>>"Hello %s" %(name) #'Hello Amy'

# %s : → (name) 으로 대체된다. 
# %(name)의 %은 %s와 (name)을 잇는 연결고리 역할을 한다.
```

```python
day = 7
>>>"03 - %s - 2018" %(day) # '03 - 7 - 2018'
>>> "03 - %02d - 2018" %(day) # '03 - 07 - 2018'
# %s 는 문장 끝에 있는 (day)와 대체된다.
# %02d 는 정수인 %d에 0과 2 옵션 두개가 추가되었음. 
# 0은 숫자 앞에 0을 붙인다는 뜻, 2는 숫자 옆에 한칸을 띄우겠다는 뜻이다.
```

```python
string_1 = "market"
string_2 = "carrots"
>>>"when you go to the %s, please buy some %s" %(string_1, string_2)
#"when you go to the market, pleease buy some carrots"
# 첫번째 %s에 string_1
# 두번째 %s에 string_2  을 대입한다.
```

참고: [https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=happyrachy&logNo=221224309880](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=happyrachy&logNo=221224309880) (HappyRachy, [파이썬] %%d(정수), %s(문자열)

## chr()
- 유니코드 값을 입력받아 코드의 해당 문자 출력

```python
chr(97) # 'a'
chr(44032) # '가'
```

참고 : [https://sinaworld.co.kr/32](https://sinaworld.co.kr/32)

💡 깨알지식
**try - accept 예외 처리문**

> 일반적으로 프로그램 수행 도중에 예외가 발생하면 프로그램은 예외 메시지를 표시하고 자동 종료됩니다.만일 서버 프로그램처럼 종료되면 안되는 프로그램이라면 예외 처리를 하여 프로그램 종료를 막을 수 있습니다.예외가 발생할 부분을 try영역에 지정하고 except영역에서 예외를 처리할 코드를 작성해주면 됩니다.
> 

```python
기본구조
try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...

#예시
try:
    1/0
except Exception as e:
    print('Exception occured :', str(e))

#result
#Exception occured : division by zero
```

출처: [https://choseongho93.tistory.com/256](https://choseongho93.tistory.com/256) [TROLL:티스토리]

### **for _ in range()** : 
변수 이름을 _로 적어준 것으로 **보통 언더스코어로 변수명을 해줄 땐 딱히 그 변수값을 사용하지 않는다는 의미**. 즉 의미없는 값으로 단순 반복횟수만 채울 때 저렇게 함.
(크게 신경쓰지 않아도 되는 변수라 생각하면 됨)