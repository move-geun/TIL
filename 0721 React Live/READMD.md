# React로 Front-End 개발 시작해보기

---

### CRA(Create React App) :

tool로써, 실제 현업에서는 잘 안 쓰지 않을까? (기본 세팅이 많아 커스터마이징이 까다롭다)

`create-react-app`을 통해 기본 뼈대를 만들면 `babel`과 `webpack`이 기본적으로 포함되어 있다



#### 설치 및 시작

1. `Nodejs`설치 
2. 터미널에서 `npx create-react-app <앱이름>`을 통해 설치
3. `npm start` 를 통해 웹이 실행되는지 확인한다.



### 데이터 전달하기 

#### 1. `{ }` 중괄호로 묶기

```javascript
function App() {
    
    let title = ['이름', '전공'];
    
    return(
        <div>
            <span>{ title[0] }</span>
            <span>{ title[1] }</span>
        </div>
	);
}
```

`title[0]`과 같이 직접 전달하는 것이 아니라 `{}`중괄호로 묶어 데이터를 전달시킨다.

즉 `{ title[0] }`으로 데이터를 전달시켜 줄 수 있다.



#### 2. useState로 전달 및 값 변경시켜주기

```javascript
import { useState } from 'react';

function App() {
    
    let [title, titleUpdate] = useState(['나이', '주소']); 
    
    return(
        <div>
        	<button onClick={()=> {titleUpdate(['이름', '전공']) } } Update </button>
            <span>{ title[0] }</span>
            <span>{ title[1] }</span>
        </div>
	);
}
```

`useState`를 통해 title의 기본 값은 ['나이','주소'] 로 전달되고 있다.

버튼을 클릭할 경우 `titleUpdate` 함수를 통해 title의 값이 [ '이름', '전공' ]으로 변경되어 전달된다.



#### 3. `Component & map()` :

 python의 for 문과 비슷함. 요소가 있다면 요소들을 반복 시켜줌

```javascript
import { useState } from 'react';

function App() {
    
    let [title, titleUpdate] = useState(['나이', '주소']); 
    
    return(
        <div>
        	title.map((title,i) => {
                return (
                    <Trcomp column={ title[i] } />
                )
            })
        </div>
	);
    
    // component
    function Trcomp(props){
        return (
        <tr>
            <th scope="row">{props.column}</th>
        </tr>)
    }
}
```

Trcomp라는 컴포넌트를 만들었고, 그 컴포넌트는 `props.column` 으로 선언된 값을 받아온다

현재 `title`은 `['나이', '주소']` 로 구성되어있고, map을 통해 각 요소를 `Trcomp` 로 전달해주고 있다.



