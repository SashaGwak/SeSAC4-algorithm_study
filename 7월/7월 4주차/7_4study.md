# [7월 4주차] Python Summary

## **아스키코드(unicode)**
전세계 모든 문자를 컴퓨터에서 일관되게 표현하고 다룰 수 있도록 설계된 산업표준 
값을 구할때 ord(), chr() 함수를 사용한다.

### ord()
문자 → 유니코드값 반환하는 함수

```python
>>> ord('a')
97
>>> ord('가')
44032
```

### chr()
유니코드값 → 코드에 해당하는 문자 반환하는 함수

```python
>>> chr(97)
'a'
>>> chr(44032)
'가'
```
출처: [https://wikidocs.net/32#chr](https://wikidocs.net/32#chr) wikidocs, 05-5 내장 함수

## Slice()
- a[<start>:<end>:<step>]  // a는 연속적 객체들의 자료구조 ex)리스트, 튜프, 문자열
- 슬라이싱 할 시작점 : 종료점 (end는 포함 X) : 증가폭
- **리버스 인덱스**
    - 기존 인덱스와 다르게 **마지막 값부터 [-1]로 시작해서 처음 값으로 올라간다.**

```python
#예시
countries = ['Korea', 'America', 'Spain', 'Germany', 'Mexico', 'Vietnam']
print(countries[0:2]) // ['Korea', 'America']
print(countries[3:]) // ['Germany', 'Mexico', 'Vietnam']

#예시2
countries = ['Korea', 'America', 'Spain', 'Germany', 'Mexico', 'Vietnam']
print(countries[-6:]) 
print(countries[:])
print(countries[-10:10]) // 세개 모두 ['Korea', 'America', 'Spain', 'Germany', 'Mexico', 'Vietnam']

#예시3
a = '1234'
a[::-1]
result: '4321'
```

- [::-1]
    - 마지막 인덱스부터 역순으로 센다. 자주 쓰이는 기능!

### len() : list 요소의 총 개수를 구하는 함수


### list.count() : 특정 요소 개수를 구하는 함수
```python
i = [1, 2, 3, 4, 5, 5]

print(len(i)) # 리스트 요소의 총개수 # 6

print(i.count(5)) # 리스트 요소 중 5은 몇 개인지 # 2
```

## flag(Bool 변수)
- 참과 거짓으로 값을 설정
    
    ```python
    flag = True
    print(type(flag)) # <class 'bool'>
    print(flag)  # True   
    
    flag = not flag
    print(flag)  # False 
    
    if flag:
        print("참 실행")
    else:
        print("거짓 실행") # 거짓 실행
        flag = not flag
    
    if flag:
        print("참 실행") # 참 실행 
    else:
        print("거칫 실행")
    ```
    

## 재귀함수(Recursive Function)
- 자기 자신을 호출하는 함수
- basecase와 recursive case 나눠서 생각해줘야함 !
    - basecase : 0!과 같이 재귀적으로 문제를 해결할 필요 없이 바로 답을 알 수 있는 경우(=따로 풀어야 할 부분문제가 없음)
    - recursive case: 재귀적으로 부분문제를 푸는 경우 5!를 풀기 위해서 그의 부분 문제인 4! 를 풀면 되고 4!를 풀기 위해서는 →3! 3!를 풀기 위해서는 →2! 푸는 것. 
    - 재귀함수의 가장 대표적인 사용 예제는 팩토리얼(Factorial)이다. 
    - (예시 참고는 [https://velog.io/@anjaekk/알고리즘-재귀함수Recursive-Function](https://velog.io/@anjaekk/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98Recursive-Function) 에서 함)
    

### 자연수 1부터 n까지의 합 재귀함수로 만들기
```python
# 1부터 n까지의 합을 리턴
def triangle_number(n):
    if n == 1:  # basecase 
        return 1
    return triangle_number(n-1) + n # recursive case
```

### 재귀함수의 단점
-콜스택이 너무 많이 쌓여서 한계점에 도달하게 되는 Stack Overflow Error 발생할 수 있음(재귀 함수 호출이 너무 많으면) 
-파이썬은 애초에 콜스택 1000개까지 허가 
- `Call Stack?` 
함수가 끝나면 어디로 들어갈지 알아야하니 컴퓨터는 내부적으로 위치를 기억해놓는다 → Call Stack 에 저장 → 함수가 끝나면 다시 원래 위치로 돌아와 기록을 지움

💡깨알지식
**피보나치 수열**
: **첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열**

0, 1부터 시작한다.

ex) 0, 1, 1, 2, 3, 5, 8, 13, 21, …

cf) 동적계획법(다이내믹 프로그래밍)

**한수**
- 어떤 양의 정수의 각 자리가 등차수열을 이루는 수 
- 등차수열이란 연속된 두 개의 수의  차이가 일정한 수열을 의미함

**reversed() vs reverse()**
- reversed()
    - 주어진 자료구조에 담긴 원소들을 역순으로 순회할 수 있도록 반복자(iterator)를 결과값으로 반환한다. **반복자 타입**을 사용한다. 

- reverse()
    - 리스트 내에 원소들이 제자리에서 역방향으로 재배치가 된다. 조심해야 할 것은, 어떤 리스트를 상대로 reverse() 함수를 호출하면 실제로 해당 리스트에 변경을 가해진다는 것.

- 요약: 리스트의 구조를 보존하면서 결과값을 반환할 경우 reversed() 사용하자. 
(출처: [https://www.daleseo.com/python-reversed/](https://www.daleseo.com/python-reversed/) )

**할당연산자**
| Operator | Description | Example |
| --- | --- | --- |
| = | 왼쪽 변수에 오른쪽 값을 할당한다 | c = a + b → c = a + b |
| += | 왼쪽 변수에 오른쪽 값을 더하고 결과를 왼쪽변수에 할당 | c += a → c = c + a |
| -= | 왼쪽 변수에서 오른쪽 값을 빼고 결과를 왼쪽변수에 할당 | c -= a → c = c - a |
| *= | 왼쪽 변수에 오른쪽 값을 곱하고 결과를 왼쪽변수에 할당 | c *= a → c = c * a |
| /= | 왼쪽 변수에서 오른쪽 값을 나누고 결과를 왼쪽변수에 할당 | c /= a → c = c / a |
| %= | 왼쪽 변수에서 오른쪽 값을 나눈 나머지의 결과를 왼쪽변수에 할당 | c %= a → c = c % a |
| **= | 왼쪽 변수에 오른쪽 값만큼 제곱을 하고 결과를 왼쪽변수에 할당 | c **= a → c = c ** a |
| //= | 왼쪽 변수에서 오른쪽 값을 나눈 몫의 결과를 왼쪽변수에 할당 | c //= a → c = c // a |

**def**
함수 선언. function과 같은 기능