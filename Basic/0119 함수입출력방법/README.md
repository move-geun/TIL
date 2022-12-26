### **<함수>**

---

### ✔ 사용자 함수 

```python
def function_name(parameter):
	return returning_value
```

---

###  ✔ 함수 기본 구조

* **선언과 호출** 

  * def  키워드 활용

  * 들여쓰기를 통해 실행 코드 작성

  * 함수는 parameter를 넘겨줄 수 있음

  * `return` 을 통해 결과값 전달

    * ex)  입력 받은 수를 세제곱하여 반환하는 함수 tri를 작성하시오.

    ```python
    def tri(a):
        return a*a*a
    ```

* * 

---

### ✔ 입력

```python
def function(argument, argument2):
	print('f{argument}랑 {argument2}를 받았습니다.')
```

* Argument란 함수의 parameter를 통해 전달되는 값

* 함수 종류에 따라 반드시 전달되거나, 전달하지 않아도 된다.

* 여러개가 전달될 수 있으며, 기본적으로 위치에 따라 전달 됨

* **Keyword Argument**

  * ```python
    def function(argument, argument2):
    	print('f{argument}랑 {argument2}를 받았습니다.')
    function(argument='abc', argument2=36)
    #'abc'랑 36를 받았습니다.
    ```

* **Defult Argument**

  * ```python
    def function(argument, argument2 = 2):
    	print('f{argument}랑 {argument2}를 받았습니다.')
    #기본값을 지정할 수도 있다
    ```

* **Pack/Unpack** (여러 개의 Argument처리)

  * `*`을 활용. 몇 개의 argument를 받을지 모르는 함수 정의에 사용

  * ```python
    def add(*args):
        for arg in args:
            print(arg)
    add(2)
    add(2,3,4,5)
    # 모두 가능
    ```

  * `**` 사용할 경우, dictionary 형태로 처리됨

  * ```python
    #선언
    def abc(**argss):
        for key, value in argss.items():
            print(key, ":", value)
    #호출
    abc(a='a', b='b', c='c')
    ```

* **함수 정의 주의사항**

  * ```python
    def hi(name = 'DK', age):
    	pass
    # 위와 같이 기본 argument 값을 가진 argument 다음에 기본값이 없는 argument정의 불가능
    ```

* **함수 호출 주의사항**

  * ```python
    add(x=5,6)
    # 위와 같이 keyword argument 다음에 positon argument 활용 불가능
    ```

---

### ✔ 출력

* **함수의 결과값**

  * 명시적 `return` 값이 없는 경우 `None` 반환하고 종료

  * `return` 시 값 반환 후 함수 바로 종료

  * 한 코드 안에 두 개의 `return`은 불가능

    * ex)

    ```python
    def cal_c(x,y):
        return x-y
    	return x+y
    ```

    * `cal_c(4,5)` 실행 시 , 첫 번째 `return`값 -1만 반환하고 종료

* 값을 여러개 `return` 하려면 튜플 형태로 반환 가능

  ```python
  def cal_c(x,y):
      return x-y, x+y
  cal_c(4,5) = (-1,9)
  ```

* `return`과 `print`는 다르다.

---

### ✔ 함수의 범위

* 함수는 코드 내부에 **local scope**를 생성하며, 그 외인 **global scope**로 구분

* **scope**

  * global scope : 코드 어디서든 참조 가능
  * local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능

* **variable**

  * global variable : global scope에 정의된 변수
  * local scope : local scope에 정의된 변수

* **변수 수명주기**

  * built-in scope : 영원히
  * global scope : 모듈 호출된 시점 혹은 인터프리터가 끝날 때까지
  * local scope : 함수 호출될 때 생성하고, 종료될 때까지만 유지

  ```python
  def func():
      a = 20
      print('local', a)
  #local 20
  fucn()
  print('global', a)
  #에러
  #a는 Local scope에서만 존재
  ```

* **이름 검색 규칙 LEGB Rule**

  * 식별자들은 **scope**에 따라 활용가능, 불가능으로 나뉨
  * **L**ocal scope : 함수
  * **E**nclosed scope : 특정 함수의 상위 함수
  * **G**lobal scope : 함수 밖의 변수, Import 모듈
  * **B**uilt-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성

  ```python
  a = 0
  b = 1
  def enclosed():
      a = 10
      c = 3
      def local(c):
          a = 10
          c = 3
          def local(c):
              print(a, b, c)
          local(300)
          print(a, b, c)
   enclosed()
  print(a, b)
  # 10 1 300
  # 10 1 3
  # 0 1
  ```

* **global문**

  * 현재 코드 블록 **전체**에 적용되며, 나열된 식별자가 global variable임을 나타냄

    * global에 나열된 식별자는 같은 코드 블록에서 global 앞에 등장할 수 없음

    * global에 나열된 식별자는 prameter, for 루프 대상, 클래스/함수 정의 등으로 되면 안됨

    * ```python
      #주의사항
      a = 10
      def func1():
          print(a)
          global a
          a = 3
      print(a)
      func1()
      print(a)
      
      # syntaxerror 뜸. 이미 a가 선언되어있기에
      ```

* **nonlocal문**

  * global을 제외하고 가장 가까운 scope의 변수를 연결하도록 함

    *  nonlocal에 나열된 식별자는 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
    * nonlocal에 나열된 식별자는 prameter, for 루프 대상, 클래스/함수 정의 등으로 되면 안됨

  * global과 달리 이미 존재하는 이름과 연결만 가능

  * ```python
    x = 0
    def func():
        x = 1
        def func2():
            nonlocal x
            x = 2
        func2()
        print(x)
    fucn1()
    print(x)
    ```

- ***주의***
  -  기본적으로 함수에 선언되는 변수는 Local scope에 생성되며, 함수 종료 시 사라짐
  - 해당 scope에 변수가 없는 경우 LEGB rule에 의해 이름을 검색함
    - 변수에 접근은 가능, but 해당 변수 수정 불가
    - 함수 내에서 필요한 상위 socpe 변수는 argument로 넘겨서 활용할 것 (클로저 제외)
  - 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능
    - But, 코드가 복잡해지고 오류 발생 >> *함수로 값을 바꾸고자 하면 argument로 넘기고 리턴 값을 사용*
- ***globals()와 locals()*** >> 범위 확인하기
  - namespace(global, local, builtin) 을 딕셔너리(dict)으로 정리
    - locals() : locals()가 실행되어지는 함수 내의 local namespace 들을 정리
    - globals() : global, local, builtin 정보 모두 dict 형태로 정리

---

### ✔ 함수 응용

* `map(funciton, iterable)` 

  * 순환 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용, 결과를 map object로 반환

  * ```python
    n, m = map(int,input().split())
    #input 값으로 3 5  입력
    print(n,m)
    print(type(n),type(m))
    # 3 5 
    # <class 'int'> <class 'int'>
    ```

* `filter(function, iterable)`

  * 순회 가능한 데이터 구조의 모든 요소에 함수 적용, `True`만 filter object로 반환

  * ```python
    def odd(n):
        return n%2
    numbers = [1,2,3]
    result = filter(odd,numbers)
    print(result, type(result))
    # <filter object at 0x10e4dfc10> <class 'filter'>
    # 이 상태에 result 는 [T,F,T]임
    list(result) #사용하려면 형변환을 해주어야한다
    # [1,3]
    ```

* `zip(*iterables)`

  * 복수의 iterable을 모아 듀플을 원소로 하는 zip object 반환

  * ```python
    girls = ['Jane', 'ashley']
    boys = ['justin','eric']
    pair = zip(girls, boys)
    print(type(pair))
    # <class 'zip'>
    list(pair)
    # [('jain', 'justin'),('ashley','eric')]
    # 각 요소의 갯수가 다를 경우, 작은 요소에 맞춰서 zip object 반환됨
    # zip 되는 리스트 갯수에 제한 X
    ```

* `lambda[parameter]:  표현식`

  * 표현식 결과값을 반환하는 함수, 익명함수라고 불림

  * return 문을 가질 수 없음, 간편 조건문 외의 조건이나 반복 불가

  * 함수 정의보다 간결하게 사용, `def`를 사용할 수 없는 곳에서 사용 가능

  * ```
    #삼각형 넓이 구하는 공식 
    tri_area = lambda b, h : 0.5*b*h
    tri_area(5,6)
    # 15.0
    ```

* `재귀함수`

  * 자기 자신 호출, 알고리즘에서 유용하게 사용

  * 1개 이상의 종료상황이 존재하고 그에 수렴하도록 작성

  * 최대 재귀 깊이가 1,000번으로 호출 횟수가 넘어가면 Recursion Error 발생

  * 알고리즘에선 재귀적 표현이 자연스러움

  * 재귀 호출은 변수 사용을 줄여줌

  * 재귀 호출은 값이 커질수록 연산 속도가 오래 걸림

  * ```python
    def factorial(n):
    	if n == 0 or n == 1:
    		return 1
    	else:
    		return n * factorial(n-1) #재귀함수 사용
    factorial(4)
    
    # 24
    ```

* `반복문`

  * ```python
    def fact(n):
    	result = 1
    	while n > 1:
    		result *= n
    		n -= 1
    	return result
    ```

    