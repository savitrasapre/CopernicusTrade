import React, { useEffect, useState } from "react";
import { Chart } from "react-google-charts";

export const options = {
  legend: "none",
  backgroundColor: "#212837",
  hAxis: {
    //title: "USD",
    format: "MM/dd",
    textStyle: {
      color: "#fff",
    },
    slantedText: true,
    slantedTextAngle: 45,
  },
  vAxis: {
    gridlines: {
      count: 0,
    },
    title: "Price",
    textStyle: {
      color: "#fff",
    },
  },
  seriesType: "candlesticks",
  series: {
    1: {
      type: "line",
      color: "#15135b",
      lineWidth: 2,
      pointSize: 0,
    },
  },
  candlestick: {
    fallingColor: { strokeWidth: 0, fill: "#f6465d" }, // red
    risingColor: { strokeWidth: 0, fill: "#0ccb80" }, // green
  },
};

const CandlestickChart = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  console.log(data);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          "http://34.41.7.45:8000/broker/chart/ma/AAPL"
        );
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const result = await response.json();
        result?.chart_data?.unshift([
          "Date",
          "Open",
          "High",
          "Low",
          "Close",
          "MA",
        ]);

        setData(result?.chart_data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []); // Empty dependency array means it runs once when component mounts.

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <Chart
      width={"100%"}
      height={"100%"}
      chartType="ComboChart"
      loader={<div>Loading Chart</div>}
      data={data}
      options={options}
      style={{ minHeight: "500px" }}
    />
  );
};

export default CandlestickChart;
