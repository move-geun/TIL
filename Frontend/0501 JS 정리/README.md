### JS 평가 대비

---

1. 데이터 타입들을 잘 알아야한다

   1. 원시타입 (Primitive type)

      객체가 아닌 기본 타입, 변수에 해당 타입 값이 담김

      다른 변수 복사시 실제 값 복사

      ex) Number, String, Boolean, undefined, null, Symbol

   2. 참조타입(Reference type)

      객체 타입 자료형, 변수에 해당 객체의 참조값이 담김

      다른 변수 복사시 참조 값 복사

      ex) Objects, Array, Function, ..etc



2. 변수 선언 관련
   1. 변수 선언 => const, let, var 
   2. 함수 선언
      1. 함수 선언/함수 표현



3. JavaScript의 설계자 => 브랜던 아이크

   1. 팀 버너스리 = 웹을 만든 사람
   2. 리누스 토르발스 = 깃, 리눅스 만든 사람
   3. 귀도 반 로섬 = 파이똔 만든 사람

   

4. array 접근 방법, 데이터 접근 방법



5. const, let, var 차이점 알기

   |                          |   const    |                        let                         |             var              |
   | :----------------------: | :--------: | :------------------------------------------------: | :--------------------------: |
   |          재할당          |     X      |                         O                          |              O               |
   |          재선언          |     X      |                         X                          |              O               |
   |                          |            | 어떤 브라우저에서는 <br>let을 재선언 가능하게 해줌 |                              |
   | 스코프 어떻게 작동하는지 | 블록스코프 |                     블록스코프                     | 함수스코프 <br>호이스팅 가능 |

   | null                                 | undefined                                                    |
   | ------------------------------------ | ------------------------------------------------------------ |
   | 빈 값을 표현하기 위한 데이터 타입    | 빈 값을 표현하기 위한 데이터 타입                            |
   | 개발자가 의도적으로 필요한 경우 할당 | 변수 선언 시 아무 값도 할당하지 않으면,<br>자바스크립트가 자동으로 할당 |
   | console.log(typeof null) => object   | console.log(typeof undefined) => undefined                   |



6. 콜백함수 특징

   ​	어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수로, 다른 언어도 가지고 있는 특징

   | 메서드  |                            설명                             |                   비고                    |
   | :-----: | :---------------------------------------------------------: | :---------------------------------------: |
   | forEach |        배열의 각 요소에 대해 콜백 함수를 한번씩 실행        |                반환값 없음                |
   |   map   |     콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환      | 기존 배열 자체를 다른 형태로 바꿀 때 유용 |
   | filter  | 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열 반환 |     기존 배열 요소를 필터링할 때 유용     |
   | reduce  |    콜백 함수의 반환 값들을 하나의 값(acc)에 누적후 반환     |                 뒤에 나옴                 |
   |  find   |         콜백 함수의 반환 값이 참이면 해당 요소 반환         |      찾는 값이 없으면 undefined 반환      |
   |  some   |    배열 요소 중 하나라도 판별 함수를 통과하면 참을 반환     |         빈 배열은 항상 거짓 반환          |
   |  every  |       배열 모든 요소가 판별 함수를 통과하면 참을 반환       |          빈 배열은 항상 참 반환           |

   

7. class list에 요소 추가하는건 `add`로 추가한다



8. 화살표 함수의 특징 

   * 함수를 비교적 간결하게 정의할 수 있는 문법
   * function 키워드 생략 가능
   * 매개변수가 단 하나뿐이라면 '()'도 생략 가능
   * 함수 몸통이 표현식 하나라면 '{}'과 return도 생략 가능

   ```javascript
   const arrow1 = funcion (name) {
       return `hello, ${name}`
   }
   
   // funtion 키워드 삭제
   const arrow1 = (name) => { return `hello, ${name}`}
   
   // 매개변수 1개 일떄, () 생략
   const arrow1 = name => { return `hello, ${name}`}
   
   // 함수 바디가 return을 포함한 표현식 1개일 경우 {} return 생략
   const arrow1 = name => `hello, ${name}`
   ```

   

9. boolean 표현방법

   1. 파이썬에서는 True, False인데

      JS에서는 true, false로 사용

      어느 상황에서 무엇이 나오는지 찾아 볼 것

      ex) object가 비어있을 때도 true가 나온다

   | 데이터타입 |    거짓    |        참        |
   | :--------: | :--------: | :--------------: |
   | Undefined  | 항상 거짓  |        X         |
   |    Null    | 항상 거짓  |        X         |
   |   Number   | 0, -0, NaN | 나머지 모든 경우 |
   |   String   | 빈 문자열  | 나머지 모든 경우 |
   |   Object   |     X      |     항상 참      |

   

10. 1급 객체의 조건 3가지
    1. 변수에 할당 가능
    2. 함수의 매개 변수로 전달 가능
    3. 함수의 반환 값으로 사용 가능



11. `appendChild` 메서드 특징
    1. 한번에 오직 한개의 노드만 추가 가능하다
    2. 마지막 자식으로 삽입한다
    3. 주어진 노드가 이미 문서에 존재하는 다른 노드를 참조한다면 새로운 위치로 이동한다



12. JS에서 변수 이름 생성 3가지 방법이 있다.
    1. camelCase (두번째 단어의 첫 글자부터 대문자)
    2. PascalCase (모든 단어의 첫 글자 대문자)
    3. SNAKE_CASE (모든 단어 대문자 작성 & 단어 사이에 언더바 삽입)
    4. `_`와 `-` 둘 다 사용 불가능 (이건 무슨 말일까? // 아마 스네이크 케이스 제외하고는 못쓴다는 말인듯)



13. 객체 정의시 

    1. key와 value가 같으면 축약이 가능하다

       ```javascript
       const books = ['Learning JS', 'Learning Python']
       const magazines = ['Vogue', 'Science']
       
       const bookShop = {
           // 기존
           // books : books,
           // magazines : magazines,
           
           // 축약 후
           books,
           magazines,
       }
       console.log(bookShop)
       ```

    2. 메서드 선언 시 funcion 키워드 생략 가능

       ```javascript
       const obj = {
           greeting() {
               console.log('Hi')
           }
       }
       
       // 기존
       var obj = {
           greetin : function() {
               console.log('Hi')
           }
       }
       ```

       



14. `for ~ in`과 `for ~ of` 의 차이

    1. `for in`

       * 주로 객체 속성 순회시 사용
       * 배열도 순회가능하지만, 인덱스 순으로 순회한다는 보장이 없어 권장 X
       * 객체 순회시 키 값이 반환된다

       ```javascript
       // array
       const fruits = ['딸기', '바나나', '메론']
       
       for (let fruit in fruits){
           consol.log(fruit) 
       }
       // 0, 1, 2
       
       
       // object
       const capitals = {
           korea : 'seoul',
           france : 'paris',
           USA : 'washington D.C.'
       }
       
       for (let capital in capitals){
       	consol.log(capital)
       }
       // korea, france, USA
       ```

       

    2. `for of`

       * 반복 가능한 객체를 순회하며 값을 꺼낼 떄 사용
       * Array, Map, Set, String

       ```javascript
       // array
       const fruits = ['딸기', '바나나', '메론']
       
       for (let fruit of fruits){
           consol.log(fruit) 
       }
       // 딸기, 바나나, 메론
       
       
       // object
       const capitals = {
           korea : 'seoul',
           france : 'paris',
           USA : 'washington D.C.'
       }
       
       for (let capital of capitals){
       	consol.log(capital)
       }
       // Uncaught TypeError : capitlas is not iterable
       ```

       



15. `reduce`의 특징

    1. 배열 각 요소에 대해 콜백 함수를 한 번씩 실행
    2. 콜백 함수의 값을 하나의 값(acc)에 누적 후 반환
    3. 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

    ```javascript
    const numbers = [1, 2, 3]
    
    const result = numbers.reduce((acc, num) => {
        return acc+num
    },0)
    
    console.log(result) // 6
    ```

    

16. 기본 이벤트 동작 중단 = `event.preventDefault()`



17. 브라우저의 전역객체 = window



18. 유니코드의 모티브는 아스키코드 
    1. 정해진 값이 소문자가 큰지, 대문자가 큰지 찾아 볼 것
    2. 소문자가 더 크다
    3. 대문자 A = 65, 소문자 a = 97로 각각 할당되어있다.



19. `this` => 실행 문맥에 따라 다른 대상을 가리킨다.

    콜백 함수 내부에 있는 this는 기본적으로 window를 가르킴

    아닐 경우 메서드가 소속된 객체를 가리킴



20. 서술형 => const, let, var 외워가기

