import { useEffect, useState } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [coins, setCoins] = useState([]);

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
        <select>
          {coins.map((coin) => (
            <option key={coin.id}>
              {coin.name} ({coin.symbol}) : $ {coin.quotes.USD.price} USD
            </option>
          ))}
        </select>
      )}
      <hr />
      {/* {coin.quotes.USD.price} */}
    </div>
  );
}

export default App;
