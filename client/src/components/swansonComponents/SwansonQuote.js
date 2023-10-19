import React, { useState, useEffect } from "react";
import "../css/swanson.css";
function SwansonQuote() {
  const [quote, setQuote] = useState("");

  useEffect(() => {
    getQuote();
  }, []);

  function getQuote() {
    fetch(`https://ron-swanson-quotes.herokuapp.com/v2/quotes`)
      .then((response) => response.json())
      .then((data) => setQuote(data));
  }

  return (
    <div className="ron-container">
      <div className="display">
        <div>
          <section>
            <button
              className="swanson-button"
              onClick={() => getQuote()}
              id="fetch"
            >
              Fetch
            </button>
          </section>
          <p id="quote">{quote}</p>
          <br />
        </div>
        <img
          id="ron"
          src="https://upload.wikimedia.org/wikipedia/en/a/ae/RonSwanson.jpg"
        />
      </div>
    </div>
  );
}

export default SwansonQuote;
