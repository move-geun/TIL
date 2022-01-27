### OOP(객체지향프로그래밍)

#### 1. 객체지향 프로그래밍 (OOP)

* #### 객체

  * 객체는 특정 타입의 인스턴스

  * ```
    123,900,5는 모두 int의 인스턴스
    'hello', 'bye'는 모두 string의 인스턴스
    ```

  * | 객체의 특징 |                                               |
    | ----------- | --------------------------------------------- |
    | 타입        | 어떤 연산자(operator)와 조작(method) 가능한가 |
    | 속성        | 어떤 상태(데이터)를 가지는가                  |
    | 조작법      | 어떤 행위(함수)를 할 수 있는가                |

  * **객체지향프로그래밍이란**

    * 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

    ```python
    #절차지향 // 제일 앞 a가 할 수 있는 것이 없음. 계속 선언해주어야한다 //객체를 활용할 수 없다
    a = [1,2,3]
    a = sorted(a)
    a = reversed(a)
    #값 추가에 있어서도 append라는 함수를 따로 정의한 뒤, a에 할당해주어야함
    def append(1,value):
        return 1 + [value]
    a = append(a,4)
    ```

    ```python
    #객체지향 // a자체의 변화가 가능, 값 추가도 바로 가능 // S+V (주어+동사)로 이해하면 빠름
    a = [1,2,3]
    a.sort()
    a.reverse()
    a.append(4)
    ```

  * **객체지향 프로그래밍이 필요한 이유**

    * 프로그램이 유연하고, 변경 용이함
    * 소프트웨어 개발과 보수를 간편하게 하며, 직관적인 코드 분석이 가능

    ```python
    #절차지향의 경우 새 사람을 추가하려면, 또 dict형태를 추가해주어야함
    person = {
        'name' = '홍길동',
    	'age' = '21'
    }
    
    person_02 = {
        'name' = '홍길동2',
    	'age' = '212'
    }
    
    def greeting(person_dict):
        print(f'안녕하세요 {person.get('name')}')
    greeting(person_01)
    ```

    ```python
    #객체지향(메소드를 만든다?), 사람 추가가 간략해짐
    class Person:
        def __init__(self,name,gender):
            self.name = name
            self.gender = gender
        def greeting(self):
            print(f'안녕하세요, {self.name}입니다')
            
    jimin = Person('지민','남')
    jimin.greeting() #=> 안녕하세요, 지민입니다.
    
    jieun = Person('아이유','여')
    jieun.greeting() #=> 안녕하세요, 아이유입니다.
    ```

  * 사각형 넓이 구하기 예시

    ```python
    #절차지향 / 요소 추가시마다 새로 정의를 추가해야함
    def area(x,y):
        return x*y
    def circu(x,y):
        return 2*(x+y)
    a=10
    b=30
    c=300
    d=20
    square1 = area(a,b)
    square1_cir = circu(a,b)
    square2 = area(c,d)
    square2_cir = circu(c,d)
    ```

    ```python
    #객체지향 / 새로운 요소 추가가 쉬움
    class Rectan:
        def __init__(self,x,y):
            self.x = x
            self.y = y
        def area(self):
            return self.x+self.y
        def circu(self):
            return 2*(self.x+self.y)
    r1 = Rectan(10,30)
    r1.area()
    r1.circu()
    
    r2 = Rectan(300,20)
    r2.area()
    r2.circu()
    ```

  ---

* #### OOP기초

  ```python
  #기본 문법
  class MyClass: #클래스 정의
      pass
  
  my_instance = MyClass() # 인스턴스 생성
  my_instance.my_method() # 메소드(=클래스 내부 함수) 호출
  my_instance.my_attribue # 클래스 내부의 속성
  ```

  ---

* #### 인스턴스

  * **인스턴스 변수란?** 

    * 인스턴스들의 고유한 변수, 개인적 속성
    * `self.<name>`으로 정의

  * **인스턴스 메소드**

    * 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨]
    * 클래스 내부에 정의되는 메소드의 기본

  * `self`

    * 인스턴스 자기자신
    * 매개변수 이름으로 self를 첫번째 인자로 정의
    * 다른 단어도 가능하지만, 암묵적 규칙으로 self 사용

    ```python
    #클래스 정의(Person)
    class Person:
        #인스턴스 메서드
        #파이썬 내부에서 Person.test(p1)으로 실행됨
        def test(self):
            return self
    #인스턴스 생성(p1)
    p1 = Person()
    
    p1.test()
    
    ```

  * **생성자 메소드**(`__init__`)

    * 인스턴스 객체가 생성될 때, 자동 호출되는 메소드

    * 변수의 초깃값 설정

      ```python
      class Person :
          
          def __init__(self, name, age):
              #인스턴스 변수 정의를 위해 사용
              self.name = name
              self.age = age
              print(f'인스턴스가 생성되었습니다. {name}')
             
              
      person1 = Person('지민', 14)
      #=> 인스턴스가 생성되었습니다. 지민
      ```

  * **소멸자 메소드(`__del__`)**

    * 인스턴스 객체가 소멸되기 전 호출되는 메소드

      ```python
      class Person:
          
          def __del__(self):
              print('인스턴스가 사라졌습니다')
          
      peson1 = Person()
      del person1
      #=> 인스턴스가 사라졌습니다.
      ```

  * **매직 메소드**

    * 특수한 동작을 위해 만들어진 메소드. 특정상황에 자동으로 불려옴

    ![](https://user-images.githubusercontent.com/85543481/151088707-d9aaa641-2098-4df1-8967-846d213779cc.png)

    ```python
    class Person :
        
        def __init__(self, name, age, height):
            self.name = name
            self.age = age
            self.height = height
        def __str__(self): #기존은 print(p1) 경우 주소값이 나오지만, __str__ 추가로 prin						t 기능 사용 가능
            return f'<{self.name}> : {slef.age}살'
        def __gt__(slef, other): #greater than으로 부등호 연산자
            return self.age > other.age
        def __len__(self):
            return self.height
        
    p1 = Person('재영', 100, 180)
    p2 = Person('지선', 10, 185)
    p1 > p2 # True
    len(p1) # 180
    print(p1) #<재영> : 100살
    ```

  ---

* #### 클래스

  * **클래스 변수**

    * 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성
    * 클래스 이름 대신 인스턴스 이름을 쓰면 인스턴스 변수
    * 클래스 선언 내부에서 정의

    ```python
    class Circle :
        
        pi = 3.14 #클래스 변수(고정요소에 대해 인스턴스 변수가 아닌 클래스 변수로 저장 후 사용)
        
        def __init__(self,r):
            self.r = r
        
        def area(self):
            return Cicle.pi * self.r * self.r
        
    c1 = Circle(2)
    c2 = Circle(3)
    print(Circle.pi) # 3.14
    print(c1.area()) # 12.56
    print(c1.pi)	 # 3.14
    print(c2.pi)	 # 3.14
    ```

  * **클래스 메소드**

    * 클래스가 사용할 메소드
    * `@classmethod` 데코레이터를 사용하여 정의
    * 호출시 첫번째 인자로 클래스(cls)가 전달됨

    ```python
    class MyClass :
        var = 'Class 변수'
        
        @classmethod
        def class_method(cls): #인스턴스메소드랑 구분하기 위해 self 대신 cls를 넣는거임
           	print(cls.var)
            return cls
    
    print(MyClass.class_method()) # Class 변수 / __main__.MyClass
    print(MyClass)				  # Class 변수 / __main__.MyClass
    ```

  * **스태틱 메소드**

    * 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드
    * `@staticmethod` 데코레이터 사용하여 정의
    * 호출 시 어떠한 인자도 전달되지 않음

    ```python
    class MyClass :
    
        @staticmethod
        def static_method(): 
            return 'static'
        
    MyClass.static_method() # static
    ```
    
  * **메소드**

    ```python
    class MyClass :
        #함수는 기본적으로 로컬 스코프
        #내부에서 활용하고 싶으면 파라미터로 받도록 정의
        
        #인스턴스 메서드 : 인스턴스를 조작하고 싶어
        #(파이썬 제작자) 함수 내부에 인스턴스를 던져주도록 설계
        #메서드를 정의할 때 self로 받도록
        def instance_method(self):
            return self
        
        #클래스 메서드 : 클래스 조작하고 싶어
        #(파이썬 제작자) 함수 내부에 클래스를 던져주도록 설계
        #메서드를 정의할 때 cls로 받도록
        @classmethod
        def class_method(cls):
            print(cls.var)
            return cls
        
        #스태틱 메서드 : 클래스나 인스턴스 조작할 생각은 없는데 함수 쓸거야
        @staticmethod
        def static_method():
            return ''
    ```

    


---

#### 2. 객체지향의 핵심개념(4대개념)

* #### 추상화

  * ```python
    #대상에 따라 다르게 정의해주는 것
    class Person :  							# 사람 정의시 이름과 나이만
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    class Student : 							# 학생 정의시 gpa까지 인자로 받음
        def __init__(self, name, age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa
      
    class Professor :							# 교수 정의시 department까지 인자로 받음
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.gpa = department
    ```

  ---

* #### 상속

  * 두 클래스 사이 부모-자식 관계 정립
  * 모든 파이썬 클래스는 **object**를 상속받음
  * 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계, 제약 조건을 모두 상속 받음

  ```python 
  class Person:
      
      def __init__(self, name, age):
          self.name = name
          self.age = age
          
      def talk(self):
          print(f'반갑습니다. {self.name}입니다.')
   
  p1 = Person('윤경', 30)
  p1.talk()	# 반갑습니다. 윤경입니다.
  ######################################################
  class Professor:
      def __init__(self, name, age, department):
          self.name = name
          self.age = age
          self.department = department
  
  p1 = Professor('윤경',30,'컴공')     
  p1.talk()	# 오류남 
  ########################################################
  class Professor(Pesron):
      def __init__(self, name, age, department):
          self.name = name
          self.age = age
          self.department = department
  
  p1 = Professor('윤경',30,'컴공')     
  p1.talk()	# 반갑습니다. 윤경입니다. // class 선언시 Person을 상속받는다고 말했기 때문에 가능
  ########################################################
  class Student(Pesron):
      def __init__(self, name, age, gpa):
          self.name = name
          self.age = age
          self.gpa = gpa
      def talk(self):
          print(f'{self.name}입니다. 교수님')
  
  p1 = Student('동근',28, 4.5)     
  p1.talk() #동근입니다. 교수님 / 클래스마다 다르게 설정도 가능 == 오버라이딩이라고 함 // 
  ```

  * **상속 관련 함수와 메소드**

    * `isinstance(object, classinfo)` : classinfo의 instance거나 subclass인 경우 `True`

    * `issubclass(class, classinfo)` : class가 classinfo의 subclass면 `True` 상속관계여부

      ```python
      issubclass(bool, int)			# True
      issubclass(float, int)			# False
      issubclass(Professor, Person)	# True
      ```

    * `super()` : 자식 클래스에서 부모 클래스를 사용하고 싶은 경우

      ```python
      class Person:
          
          def __init__(self, name, age):
              self.name = name
              self.age = age
              
          def talk(self):
              print(f'반갑습니다. {self.name}입니다.')
              
      class Student(Person):
          
          def __init__(self, name, age, student_id):
              super().__init__(name, age) #Person에서 가져옴
              self.student_id = student_id
         
      s1 = Student('영주', 26, 2022)
      s1.name					# 영주
      s1.age					# 26
      ```

  * **다중 상속**

    * 두개 이상의 클래스를 상속받음
    * 중복된 속성이나 메서드의 경우 상속 순서에 의해 결정됨

    ```python
    class Person:
        def __init__(self, name):
            self.name = name
            
       def greeting(self):
        return f'안녕, {self.name}'
    
    class Mom(Person):
        gene = 'XX'
        def swim(self):
            return '엄마가 수영'
        
    class Dad(Person):
        gene = 'XY'
        def walk(self):
            return '아빠가 걷기'
    
    class FirstChild(Dad, Mom):
        def swim(self):			#엄마 수영 오버라이딩
            return '첫째가 수영'
        def cry(self):
            return '첫째가 응애'
        
    baby1 = FirstChild('애기')
    baby1.cry()			# 첫째가 응애
    baby1.swim()		# 첫째가 수영
    baby1.walk()		# 아빠가 걷기
    baby1.gene			# XY // 아빠가 먼저 상속되어서 아기 성별은 XY
    ```

    * **mro 메소드**

      * 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메소드
      * 기존 인스턴스 -> 상속인스턴스 -> 자식클래스 -> 부모 클래스로 확장

      ```python
      FirstChild.mro()
      # [__main__.FirstChild, __main__.Dad, __main__.Mom, __main__.Person, object]
      ```

  ---

* #### 다형성(메소드 오버라이딩)

  * 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음을 의미
  * 서로 다른 클래스에 속해있는 객체들이 동일 메세지에 대해 다른 방식으로 응답될 수 있음
  * 상속 받은 메소드를 재정의(위에서 엄마 수영과 첫째 수영이 다른거 처럼)

  ---

* #### 캡슐화

  * 파이썬에서 암묵적으로 존재하지만, 언어적으로 존재하지 않음

  * 객체의 일부 구현 내용에 대한 외부로부터 직접적인 엑세스를 차단

  * `Public Access Modifier` : 어디서나 가능

    * 언더바 없이 시작하는 메소드나 속성, 어디서나 호출 가능, 하위 클래스 override 허용

  * `Protected Access Modifier` : 상속 관계에만 가능 // 실제적으로 없음

    * 언더바 1개로 시작, 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
    * 하위 클래서 override 허용

    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self._age = age			#protected access modifier
        
        def get_age(self):
            return self._age
    
    p1 = Person('송지', 23)
    p1.age()				# 오류 (일반적으로 사용하는 방식이 아닌
    						# 언더바 하나를 넣음으로 정보 보호역할)
    p1.get_age()			# 23
    p1._age					# 23 / 이렇게 직접 접근해도 확인 가능하지만 암묵적으로 활용
    ```

  * `Private Access Modifier` : 본인 내부에서만 가능
  
    * 언더바 2개로 시작, 본 클래스 내부에서만 사용 가능
    * 하위 클래스 상속 및 호출 불가, 외부 호출 불가
  
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.__age = age			# _ 두 개로 private 설정
        
        def get_age(self):
            return self.__age
    
    p1 = Person('아이', 30)
    p1.get_age()			# 30
    p1.__age				# 불가능
    #언제 사용하냐? 여기서 name과 age 두개를 받아오지만, age는 private하게 만들고 싶을 때.
    #
    ```
  
  * **getter 메소드와 setter 메소드**
  
    * 변수에 접근할 수 있는 메소드를 별도로 생성
      * **getter 메소드** : 변수의 값을 읽는 메소드
      * `@property` 데코레이터 사용
      * **setter 메소드** :  변수의 값을 설정하는 성격의 메소드
      * `@변수.setter` 사용
  
    ```python
    #데코레이터 사용한 getter/setter 사용방법
    class Person:
        
        def __init__(self, age):
            self.__age = age		#private 설정
            
        @property
        def age(self):				#getter
            return self.__age
        
        @age.setter
        def age(self, value):		#setter
            self.__age = value
        
    p1 = Person(40)
    p1.age()		    # private이라 출력 안됨
    print(p1.age)	    # 40  @property를 붙여서 속성처럼 사용 가능 
    p1.age = 33         # private 이라 접근불가지만, setter 데코를 사용하여 값 변경 가능.
    print(p1.age)       # 33	
    ```
    
    ```python
    #데코레이터 없이 getter/setter 사용법
    class Person():
        
        def __init__(self,age):
            self.__age = age		#private 설정
            
        def get_age(self):			#getter
            return self.__age
        
        def set_age(self, value):	#setter
            self.__age = value
      
    p1 = Person(40)
    p1.age()		        # private이라 출력 안됨
    print(p1.get_age())	    # 40  
    p1.set_age(33)          # private 이라 접근불가하지만, 
    					    # .set_age() 를 통해 값 변경 가능
    print(p1.get_age())	   # 33	
    ```
    
    