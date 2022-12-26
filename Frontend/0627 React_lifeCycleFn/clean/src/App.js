import { useEffect, useState } from "react";

// cleanUpFn : 컴포넌트가 사라질 때, 특정 함수 실행이나 정보를 전달할 수 있게 도와주는 함수
// useEffect의 마지막에 필요한 함수나 정보를 return 함으로써 컴포넌트 삭제시 원하는 함수나 정보를 실행시킬 수 있다
function Hello() {
  // 원래 작동 원리
  //   function byFn() {
  //     console.log("bye :(");
  //   }
  //   function HiFn() {
  //     console.log("create :)");
  //     return byFn;
  //   }
  //   useEffect(HiFn, []);

  // 통상적인 방법
  useEffect(() => {
    console.log("create:)");
    return () => {
      console.log("bye :(");
    };
  }, []);

  // 같은 작성법
  // useEffect(function HiFn() {
  //   console.log("create :)");
  //   return function byFn() {
  //     console.log("bye :(");
  //   };
  // }, []);
  return <h1>Showing!</h1>;
}
function App() {
  const [showing, setShowing] = useState(false);

  function onClick() {
    setShowing(!showing);
  }
  return (
    <div>
      {showing ? <Hello /> : null}
      <button onClick={onClick}>{!showing ? "Show" : "Hide"}</button>
    </div>
  );
}

export default App;
