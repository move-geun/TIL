## 📃**CSS Layout**

- ##### 블록 > 마진 우측 auto

  - div, h1,p(문단)

- ##### 인라인 > 컨텐츠로 사이즈 지정 / 높이 너비 직접 적용 안됨 

  - span, input, img

- ##### positioning

  - absoulte : static이 아닌 부모
  - fixed : 브라우저 (viewpoint)
  - relative

- ##### 10rem => 160px (root - > 16px)

---

##### 1. float - 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함

- 요소가 Normal flow를 벗어나도록 함 > 부모 요소 높이 0이 되게 함 = > clearing

- left : 요소를 왼쪽으로 띄움

- right : 요소를 오른쪽으로 띄움

- ###### **`float clearing` > float 요소의 부모로 div 안에 넣어주고 <u>부모에게 .clearfix 클래스 부여</u>**

  -  부모 높이 지정하게 해줌

  - ``` css
    .clearfix::after {
    	content: "";
    	display: block;
    	clear: both;
    }
    ```

---



##### 2. Flexbox ⭐

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

- 축

  - 메인 축
  - 교차 축

- 구성 요소

  - Flex Container(부모 요소)
  - Flex Item(자식 요소)

  

##### 	<배치 설정>

- ###### `flex-direction`

  -  row / row-reverse
  - column (축끼리 바뀜) / column-reverse

- ###### `flex-wrap` :  아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정

  - wrap : 넘치면 다음 줄로 배치 / nowrap(기본값) : 한 줄에 배치

- `flex-flow` : direction과 wrap에 대한 설정 값을 차례로 작성



##### 	<공간 나누기>

- ###### `justify-content` : 메인축 기준

- ###### `align-content` : 크로스축 기준

  - flex-start / end / center
  - space-between : 아이템 사이 균등한 공백 
  - space-around :  아이템 둘러싼 영역을 균일하게 분배 (가질 수 있는 영역을 반으로 나눠서 양쪽으로)
  - space-evenly : 전체 영역에서 균등하게 분배



##### 	<정렬>

- ###### `align-items` : 모든 아이템에 적용

- ###### `align-self` : 개별 아이템에 적용

  - stretch : 컨테이너를 가득 채움 / flex-start / end / center / baseline : 텍스트 baseline에 기준선을 맞춤



- 수직 수평 가운데 정렬

``` css
.container {
    display: flex;
    justify-content : center;
    align-items : center;
}

/* 방법 2 */
.container {
    display: flex;
}
.item {
    margin: auto;
}
```

- 카드 배치

``` css
/* 반시계 2*3*/
layout {
    display : flex;
    flex-direction : column;
    flex-wrap: wrap;
    justify-content: space-around;
    align-content: space-around;
}

/* 시계 3*2*/
layout {
    display : flex;
    flex-direction : row;
    flex-wrap: wrap;
    justify-content: space-around;
    align-content: space-around;
}
```



- `flex-grow `: 남은 영역을 아이템에 분배
- order : 배치 순서

``` css
order -3
order 1
...
order 0 > 기본
```







