import { useEffect, useState } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  const getMovies = async () => {
    const json = await (
      await fetch(
        "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt=20120101"
      )
    ).json();
    setMovies(json.boxOfficeResult.dailyBoxOfficeList);
    setLoading(false);
  };
  useEffect(() => {
    getMovies();
  }, []);

  return (
    <div>
      {loading ? (
        <h1>Loding..</h1>
      ) : (
        <div>
          <h1>Movie Recommend Site</h1>
          {movies.map((movie) => (
            <div>
              <h3>{movie.movieNm}</h3>
              <h5></h5>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
