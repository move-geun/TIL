## VanillaJs VS ReactJS

### 코드의 차이

ex- 버튼을 클릭하면 총 토탈 수가 올라가는 홈페이지를 만들어보자

`VanillaJS`

```html
<!DOCTYPE html>
<html lang="en">
<body>
  <span>Total clicks : 0</span>
  <button id="btn">Click me!</button>
</body>
<script>
  const button = document.getElementById("btn");
  const span = document.querySelector("span");
  let counter = 0;
  function handleClick() {
    console.log("Click")
    counter = counter + 1;
    span.innerText = `Total clicks : ${ counter }` 
  }
  button.addEventListener("click", handleClick);
</script>
</html>
```



`React - hard.ver` -- 사실상 안 쓴다.(그냥 React가 어떻게 작동하는지 알기 위해서 작성해 본 코드)

```react
<!DOCTYPE html>
<html lang="en">
<body>
  <div id="root"></div>
</body>
// React를 사용하기 위해 script에 넣어줘야함
<script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
<script>
  const root = document.getElementById("root");
  const span = React.createElement(
    "span", 
    null,
    "Total clicks : 0"); // property가 null인 span 생성하기
  const button= React.createElement(
    "button",
    {
      onClick:()=> console.log("im clicked"),
      id:"btn"
    },
    "Click me!"); // property에서 onclick이벤트가 붙어있는 id가 btn인 button 생성
     // container라는 div 생성 후, 우리가 만든 span, button 넣어주기
  const container = React.createElement("div", null, [span, button]);
  ReactDOM.render(container, root);  // body 안, root안에 우리가 만든 container 위치 시키기
</script>
</html>
```



#### Vanilla Code와 React Hard Code 차이

**Vanilla Code** - html 요소를 먼저 생성 후, JS를 통해 event를 달아줌

**React Hard Code** - JS를 통해 요소를 먼저 생성 후 event 만들어주고 html로 편입시켜줌



---

#### JSX란?

JSX는 자바스크립트의 확장버전, 객체를 표현한다
\- HTML 이랑 문법 구조가 비슷
\- 리액트는 JSX문법을 사용, 그러나 브라우저는 JSX문법을 이해하지 못함
\- Babel을 사용하면 브라우저가 이해할 수 있도록 JSX 문법을 변환해줌
\- 스크립트 태그를 추가하고 리액트를 작성하고 있는 스크립트 태그에 type="text/babel"을 넣어줌

`React - Easy.ver(Use JSX)` - 사실상 react에서 사용하는 방식

```react
<!DOCTYPE html>
<html lang="en">
  <body>
    <div id="root"></div>
  </body>
  <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script type="text/babel">
    const root = document.getElementById("root");
    // const Span = () => <span>Total clicks : 0</span>;  화살표 함수로 생성
    function Span() {
      return <span>Total clicks : 0 </span>;
    }
    const Button = () => (
      <button onClick={() => console.log("im clicked")}>Click me!</button>
    );
    const Container = () => (
      <div>
        <Span />
        <Button />
      </div>
    ); // <span />으로 적을 경우 html span 태그로 인식하기 때문에, 함수는 대문자로 만들어주어야 한다
    ReactDOM.render(<Container />, root);
  </script>
</html>

```



예제와 같은 코드로 생성하기 

**Ver.1 (비추천)**

```react
<!DOCTYPE html>
<html lang="en">
  <body>
    <div id="root"></div>
  </body>
  <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script type="text/babel">
    const root = document.getElementById("root");
    let counter = 0;
    function Counter() {
      counter = counter + 1;
      render();
    }
    function Container() {
      return (
        <div>
          <span>Total clicks : {counter}</span>
          <button id="btn" onClick={Counter}>
            Click me!
          </button>
        </div>
      );
    }
    function render() {
      ReactDOM.render(<Container />, root);
    }
    render();
  </script>
</html>

```

해당 코드는 `click`이 일어날 때마다 매번 render() 함수가 발생하게 되어 있다.

1. `render` 함수, 페이지 로딩시 실행 - `Container`함수 실행
2. 클릭마다 `Counter` 함수 실행 -> `render` 함수 실행 -> `Container` 함수 실행
3. 하지만 react는 똑똑하기 때문에 html 전체가 렌더링 되는게 아니라 바뀌는 counter 부분만 렌더링 해준다.

react의 강력한 부분이지만 더 나은 방법이 있다.



**Ver.2 (Best 추천)**

`React.useState()` : 초기값을 정해주고, 그 값을 변환시켜주고 해당 값을 렌더링해주는 함수를 제공

```javascript
const data = React.useState();
console.log(data);

// [undefined,f]
// undefined는 초기값을 주지 않아서 나온 값, f는 값을 변환시켜주는 함수
const data2 = React.useState(0);
console.log(data2)
// [0, f]
```

`JS에서 배열 쉽게 뽑기`

```javascript
// 기존 방식
const x = [1,2,3];
const a = x[0];
const b = x[1];
const c = x[2];

console.log(a)	// 1
console.log(b)	// 2
console.log(c)	// 3

// JS에서 제공하는 강력한 기능
const x = [1,2,3]
const [a,b,c] = x
console.log(a)	// 1
console.log(a)	// 2
console.log(a)	// 3
```

```react
<!DOCTYPE html>
<html lang="en">
  <body>
    <div id="root"></div>
  </body>
  <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script type="text/babel">
    const root = document.getElementById("root");
    function App() {
      const [data, setData] = React.useState(0);
      function onClick() {
        return setData(data + 1);
      }
      return (
        <div>
          <span>Total clicks : {data}</span>
          <button onClick={onClick}>Click me!</button>
        </div>
      );
    }
    ReactDOM.render(<App />, root);
  </script>
</html>

```

