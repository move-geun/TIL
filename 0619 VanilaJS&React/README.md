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

```html
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

```html
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



