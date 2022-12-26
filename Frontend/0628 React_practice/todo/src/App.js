import { useState } from "react";

function App() {
  // todo 입력값 관리할 state
  const [todo, setTodo] = useState("");
  // todo list 관리할 state
  const [todos, setTodos] = useState([]);
  // input에 값 입력시 받아올 function
  function onChange(event) {
    setTodo(event.target.value);
  }
  // form 제출시 작동할 function
  function onClick(event) {
    // 기본 submit event 제어
    event.preventDefault();
    // 빈값일 경우 todo에 추가되지 않도록 제어
    if (todo === "") {
      return;
    }
    // 최근 array를 받아오고, 입력된 todo를 추가해주는 코드
    // array의 경우 ...을 통해 unpack 가능하다.
    setTodos((currentArray) => [todo, ...currentArray]);
    // 입력이 끝나면 input 값을 빈값으로 초기화 해주자
    setTodo("");
  }
  // map 함수 => array에 포함된 각 요소에 적용시킬 함수를 넣어줄 수 있다
  // 첫째 인자로 각 개별요소를 받아오며, map을 사용할 때 key 값이 필요하기에 index값으로 key를 설정해줌
  return (
    <div>
      <h1>To do List ({todos.length})</h1>
      <form onClick={onClick}>
        <input
          value={todo}
          onChange={onChange}
          type="text"
          placeholder="Please Enter your To do.."
        ></input>
        <button>Add To do</button>
        <hr />
        <ul>
          {todos.map((todo, index) => (
            <li key={index}>{todo}</li>
          ))}
        </ul>
      </form>
    </div>
  );
}

export default App;
