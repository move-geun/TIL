###  React State Practice

####  Use `  for` & `class`  in React

1. html : `label`-`input` 과 같이 `for`로 연결될 경우 그냥 사용하면 된다.

   ```html
   <div>
       <span>Super Converter</span>
       <label for="minutes">Minutes</label>
       <input id="minutes" placeholder="Minutes" type="number" />
       <label for="hours">Hours</label>
       <input id="hours" placehodler="Hours" type="number" />
   </div>
   ```



2. JSX - `production.min.js` 에서는 오류 안나지만, `develope.min.js`에서는 인식 못함

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
         return (
           <div>
             <span>Super Converter</span>
             <label for="minutes">Minutes</label>
             <input id="minutes" placeholder="Minutes" type="number" />
             <label for="hours">Hours</label>
             <input id="hours" placehodler="Hours" type="number" />
           </div>
         );
       }
       ReactDOM.render(<App />, root);
     </script>
   </html>
   
   ```

   ```
   JSX에서는 
   class => className
   for => htmlFor
   로 사용해야 함
   ```




시간 - 분 단위변환 만들기 연습 예시

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
      // 입력값 state 설정
      const [minutes, setMinutes] = React.useState();
      // 입력값 받아오는 함수
      function onChange(event) {
        setMinutes(event.target.value);
      }

      // disable 변환 => 시간 입력, 분 입력 변환
      const [inverted, setInverted] = React.useState(false);
      // invert 전환 함수
      function stateInverted() {
        setInverted(!inverted);
        setMinutes("");
      }

      // reset 버튼
      function onClick() {
        setMinutes(0);
      }

      return (
        <div>
          <h2>Super Converter</h2>
          <div>
            <label htmlFor="minutes">Minutes</label>
            <input
              value={inverted ? minutes * 60 : minutes}
              id="minutes"
              placeholder="Minutes"
              type="number"
              disabled={inverted}
              onChange={onChange}
            />
          </div>

          <div>
            <label htmlFor="hours">Hours</label>
            <input
              value={!inverted ? minutes / 60 : minutes}
              id="hours"
              placeholder="Hours"
              type="number"
              onChange={onChange}
              disabled={!inverted}
            />
          </div>
          <button onClick={onClick}>Reset</button>
          <button onClick={stateInverted}>
            {inverted ? "That Back" : "Inverted"}
          </button>
        </div>
      );
    }
    ReactDOM.render(<App />, root);
  </script>
</html>

```



#### Select 옵션을 통해 필요 컴포넌트 렌더링하기

1. useState를 통해 select에 사용할 배열을 생성해준다

2. 각 option에 사용할 index를 부여해주고

3. if 문을 통해 필요 컴포넌트를 렌더링 해준다.

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
   
       function MinutesToHours() {
         return (
         <div></div>
         )
       }
       function KmToMiles() {
         return (
         <div></div>
         )
       }
   
       // select option을 사용해서 필요 컴포넌트 렌더링하기
       // 각 인덱스에 value를 주어주고, value가 선택될 경우
       // value에 맞는 컴포넌트를 렌더링 해주는 방식
       function App() {
         const [index, setIndex] = React.useState("xx");
         function onChange(event) {
           setIndex(event.target.value);
         }
         return (
           <div>
             <h3>Super Converter</h3>
             <select value={index} onChange={onChange}>
               <option value="xx">Select Converter Option</option>
               <option value="0">Minutes & Hours</option>
               <option value="1">Km & Miles</option>
             </select>
             <hr />
             {index === "xx" ? "Select Converter Option" : null}
             {index === "0" ? <MinutesToHours /> : null}
             {index === "1" ? <KmToMiles /> : null}
           </div>
         );
       }
       ReactDOM.render(<App />, root);
     </script>
   </html>
   
   ```

   
