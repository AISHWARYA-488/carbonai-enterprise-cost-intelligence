import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://localhost:8000/api/data")
        .then((res) => res.json())
        .then((json) => setData(json));
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ background: "#0f172a", minHeight: "100vh", padding: "30px", color: "white", fontFamily: "Arial" }}>
      <h1>🌍 CarbonAI Enterprise Dashboard</h1>

      <div style={{ display: "flex", gap: "20px", marginTop: "20px" }}>
        <div>
          <p>Current CO₂ (PPM)</p>
          <h2>{data.current_co2}</h2>
        </div>

        <div>
          <p>Predicted CO₂</p>
          <h2>{data.predicted_co2}</h2>
        </div>

        <div>
          <p>Estimated Savings</p>
          <h2>{data.savings}</h2>
        </div>
      </div>

      <div style={{ marginTop: "40px" }}>
        <h3>🤖 AI Recommendation</h3>
        <p>{data.suggestion}</p>
        <p>Efficiency: {data.efficiency}</p>
      </div>
    </div>
  );
}

export default App;
