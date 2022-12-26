### 디버깅

* **branches** : 모든 조건이 원하는대로 동작하는지 확인
* **for loops** : 반복문에 진입하는지, 원하는 횟수만큼 실행되는지 확인
* **while loops** : for loops와 동일, 종료조건이 제대로 동작하는지 확인
* **function** : 함수 호출 시, 함수 파라미터, 함수 결과 등을 확인
* 좀 쉬면서 다시보기, 곳곳에 print 찍어서 확인하기, 미니 러버덕 사서 설명해보기 등 여러 방법이 있다

---

### 에러와 예외

##### 1. 에러(Syntax Error)

* 실행이 되지 않음
* ex) Invalid syntax , assign to lieral, EOL(End of Line), EOF(End of File)

##### 2. 예외(Exception)

* 실행 중 만나면, 프로그램 실행을 멈춤
* 사용자 정의 예외를 만들어 관리할 수 있음
* ex) ZeroDivisionError, NameError

---

### 예외 처리

##### try/except 를 이용

* try문 
  * 오류가 발생할 가능성이 있는 코드를 실행
  * 예외가 발생되지 않으면, except 없이 실행 종료
* except문
  * 예외가 발생하면, except 절이 실행
  * 예외 상황을 처리하는 코드를 받아 적절한 조치를 취함

![image](https://user-images.githubusercontent.com/85543481/150734857-93b434b5-7090-42b7-b068-89d585588db9.png)

```python
#예외 처리 예시
try :
    num = input('숫자입력 : ')
    print(int(num))
except ValueError :
    print('숫자가 입력되지 않았습니다.')
```



##### 복수의 예외처리 실습

```python
num = input('100으로 나눌 값을 입력하시오 :')
print(100/int(num))
#이때 'a'를 입력하거나 0을 입력하면 오류가 남
#TypeError, ZeroDivisionError
```

```python
try:
	num = input('100으로 나눌 값을 입력하시오 :')
	print(100/int(num))
except (TypeError, ZeroDivisionError) :
    print('제대로 입력해라')
```



##### 예외 처리 종합 (왜쓰냐? => 에러가 뜨고 실행이 멈추는 것이 아닌, 해당 에러 발생시 관리할 수 있다면 사용하는 것)

* `try `
  * 코드를 실행함
* `except`
  * try 문에서 예외가 발생시 실행함
* `else`
  * try문에서 예외가 발생하지 않으면 실행함
* `finally`
  * 예외 발생 여부와 관계없이 항상 실행함

---

### 예외 발생 시키기

##### raise

* raise를 통해 예외를 강제 발생

* `raise  <표현식>(메세지)` : 표현식에 예외타입을 지정해야함, 없을 경우 마지막 예외를 다시 일으킴
* ![image](https://user-images.githubusercontent.com/85543481/150735985-9f55f18d-8947-4b42-b41e-d63936dc4f9f.png)

##### assert

* 상태를 검증하는데 사용되며, 무조건 AssertionError 발생
* 일반적으로 디버깅 용도로 사용
* `assert <표현식>, <메세지>` : 표현식이 False일 경우 AssertionError 발생
* ![image](https://user-images.githubusercontent.com/85543481/150736163-5f268f9c-d1a3-4c58-a135-b2bf34e102bd.png)