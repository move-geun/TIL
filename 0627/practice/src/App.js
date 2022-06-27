import { useEffect, useState } from "react";

function App() {
  const [value, setValue] = useState(0);
  const [search, setSearch] = useState("");
  function onClick() {
    setValue((prev) => prev + 1);
  }
  function onChange(event) {
    setSearch(event.target.value);
  }
  console.log("I run all times!!!");

  // function과 useEffect 분리해서 만들기
  // function onlyOne() {
  //   console.log("I run only Onetime!");
  // }
  // useEffect(onlyOne, []);

  //------------------------------
  // fuction과 useEffect 한번에 만들기
  // 1. 첫 렌더시 한번만 실행되기
  useEffect(() => {
    console.log("I run only one");
  }, []);
  // value state 값이 변경될 때만 해당 함수 실행하기
  useEffect(() => {
    console.log("I run only change Value");
  }, [value]);
  // search state 값이 변경될 때만 해당 함수 실행하기
  // search state 값이 빈값일 경우에는 검색하지 않기 => if로 조건문 걸어준 것
  useEffect(() => {
    if (search !== "") {
      console.log("I run only change Search", search);
    }
  }, [search]);
  // value와 search state 변경될 때만 해당 함수 실행하기
  useEffect(() => {
    console.log("I run change value or search");
  }, [value, search]);
  return (
    <div>
      <div>
        <input
          value={search}
          onChange={onChange}
          type="text"
          placeholder="Search Here"
        />
      </div>
      <h3>{value}</h3>
      <button onClick={onClick}>Click me!</button>
    </div>
  );
}

export default App;
