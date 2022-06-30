import { useEffect, useState } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [coins, setCoins] = useState([]);
  const [selects, setSelects] = useState(0);
  const [money, setMoney] = useState("");
  function onChange(event) {
    setSelects(event.target.value - 1);
  }
  function moneyChange(event) {
    setMoney(event.target.value);
  }
  function onClick() {
    console.log(selects);
  }
  useEffect(() => {
    // fetch로 api 받아오고
    fetch("https://api.coinpaprika.com/v1/tickers")
      // api 받아와지면 그 응답을 json 형태로 바꿔줌
      .then((response) => response.json())
      // json으로 바뀌면 coins array에 넣어주고 loading은 false로 바꿔줌
      .then((json) => {
        setCoins(json);
        setLoading(false);
      });
  }, []);
  return (
    <div>
      <h1>{loading ? "Loading..." : "Now Select Ur Coin!"}</h1>
      {loading ? null : (
        <select onChange={onChange}>
          {coins.map((coin) => (
            <option key={coin.id} value={coin.rank}>
              {coin.name} ({coin.symbol}) : $ {coin.quotes.USD.price} USD
            </option>
          ))}
        </select>
      )}
      <button onClick={onClick}>Click</button>
      <hr />
      <div>
        {loading ? null : (
          <div>
            <div>
              <input
                onChange={moneyChange}
                type="number"
                placeholder="Ur money"
              ></input>
              USD
            </div>
            <h4>
              You can have {money / coins[selects].quotes.USD.price}
              {coins[selects].name}
            </h4>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
