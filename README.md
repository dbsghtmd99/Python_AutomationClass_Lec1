# Python_AutomationClass_Lec1

첫 번째 수업은 Pycharm, Anaconda virtual environment 설정법과 기본적인 Python Syntax에 대해 학습했다.

## 1. Anaconda 가상 환경 설정하기
.py 파일을 Pycharm 으로 컴파일 시키기 위해 먼저 Anaconda prompt를 실행시켜 virtual environment 를 만들어야 한다.

이를 위해 도스창에 입력 해야 할 커맨드는 다음과 같다.

```
activate (virtual environment name) // 괄호는 생략
```

python 을 실행시킬 수 있는 환경이 만들어지면 필요에 따라 다른 개발자들이 만들어 놓은 외부 모듈을 불러올 수 있다. 이번 수업에서는 기본적인 문법만 다루기에 생략하였다.

그 다음  Pycharm 으로 들어가서 프로젝트를 만든 후 해당 프로젝트 폴더 내의 python file 에 코드를 작성하면 정상적으로 실행시킬 수 있다.

## 2. 기본 문법
기본 문법으로 자료형과 조건문, 반복문을 학습하였다.

### 2.1. 자료형
간단하게 숫자형, 실수형, 복소수형, 문자열에 대해 배우고, 리스트와 딕셔너리 그리고 튜플을 소개했다.
리스트는 우리가 아는 배열의 경우와 거의 일치한다. 리스트에 대한 자세한 관련 함수들은 Lec2에서 학습한다.

비어있는 리스트를 선언하는 방법은 다음과 같다. 
```python
newList = []
```
또는 
```python
newList = list()
```

딕셔너리는 키:값 으로 짝을 이루는 자료형이다. 리스트가 인덱스와 그 인덱스에 대응하는 요소를 가지고 있는 것 처럼,  딕셔너리는 키를 통해 그 키에 대한 값을 접근할 수 있다.

마찬가지로 비어있는 딕셔너리를 선언하는 방법은 다음과 같다. 
```python
newDict = {}
```
또는 
```python
newDict = dict()
```

딕셔너리의 키 또는 값만을 불러오기 위하기 위하여 사용하는 함수는 다음과 같다.
```python
d = {}
d.keys()
d.values()
```
```python
d = {'a':'123', 'b' : '456'}
print(d.keys())
print(d.values())
```
이를 출력해보면 키 또는 값만을 불러왔음을 볼 수 있다.
```
dict_keys(['asd', 'ddddsd'])
dict_values(['wwww', 'reseg'])
```
다음으로 튜플은 리스트와 비슷하나 마치 읽기모드로 파일을 읽듯 내부의 값을 수정 할 수 없다.

비어있는 튜플을 선언하는 방법은 다음과 같다. 
```python
newTuple = ()
```
또는 
```python
newTuple = tuple()
```
### 2.2. 조건문
기본적인 조건문은 다음과 같다.
```python
if boolean:
    statement
elif boolean:
    statement
else:
```
boolean 은 True 또는 False를 가지는 bool 자료형 이며, if, elif, else 키워드 뒤에는 콜론(:) 을 붙여주어야 한다. 또한 Python은 다른 언어와 다르게 scope 구분을 들여쓰기(indentation) 로 구분하며 이를 지키지 않으면 컴파일 에러가 발생한다.

### 2.3. 반복문
기본적인 반복문은 다음과 같다.

for문의 경우
```python
for i in iterable:
    statement
```

while문의 경우
```Python
while boolean:
    statement
```
for문의 경우 iterable 이라는 새로운 단어가 등장하는데, iterable은 '반복될 수 있는 것' 이라는 의미를 가지고 있다. 예를 들면 list 자료형의 경우 각각의 요소들이 반복될 수 있으므로 iterable 이라고 할 수 있다.
보통 for문과 range() 함수를 많이 사용하는데, python 홈페이지에 나와있는 해당 함수의 설명은 다음과 같다.

> class range(start: int, stop: int, step: int=...)

> range(stop) -> range object range(start, stop[, step]) -> range object
Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement).

즉, 요약하면 (처음, 끝) 또는 (처음, 끝, 간격) 의 매개변수를 받아 범위를 정해주고 이 객체들을 반환하는 함수이다. 1개의 매개변수만 사용할 경우 그 매개변수는 stop=으로 대입되고 start= 0이 대입되도록 defalt값이 설정되어 있다.
range 함수를 사용할 때 마지막 숫자는 포함되지 않으므로 주의 하여야한다.

while문 은 C언어와 별반 다르지 않다. while 다음에 나오는 bool 자료형이 True가 되면 반복을 계속한다.
