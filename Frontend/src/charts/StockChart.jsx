import React, { useEffect, useRef, useState } from "react";
import { Chart } from "chart.js";
import {
  CandlestickController,
  CandlestickElement,
  OhlcController,
  OhlcElement,
} from "chartjs-chart-financial";

// Register the components
Chart.register(
  CandlestickController,
  CandlestickElement,
  OhlcController,
  OhlcElement
);

const candlestickData = [
  { x: new Date("2025-03-01"), o: 100, h: 110, l: 90, c: 105 },
  { x: new Date("2025-03-02"), o: 102, h: 112, l: 91, c: 112 },
  { x: new Date("2025-03-03"), o: 103, h: 112, l: 92, c: 113 },
  { x: new Date("2025-03-04"), o: 104, h: 113, l: 93, c: 114 },
  { x: new Date("2025-03-05"), o: 111, h: 151, l: 85, c: 101 },
  { x: new Date("2025-03-06"), o: 112, h: 152, l: 84, c: 102 },
  { x: new Date("2025-03-07"), o: 113, h: 153, l: 83, c: 102 },
  { x: new Date("2025-03-08"), o: 114, h: 154, l: 82, c: 105 },
  { x: new Date("2025-03-09"), o: 115, h: 155, l: 81, c: 106 },
  { x: new Date("2025-03-10"), o: 116, h: 156, l: 80, c: 104 },
  { x: new Date("2025-03-11"), o: 117, h: 157, l: 81, c: 109 },
  // More data points...
];

const StockChart = () => {
  const chartRef = useRef(null);
  const [chartData, setChartData] = useState(null);
  console.log(chartData, candlestickData);

  useEffect(() => {
    const ctx = chartRef?.current?.getContext("2d");
    const fetchHistory = async () => {
      try {
        const response = await fetch("http://localhost:8000/broker/chart/AAPL");
        const result = await response.json();

        let xformedData = result?.history?.map((historyData) => {
          return {
            ...historyData,
            x: new Date(historyData?.x),
          };
        });

        //console.log("Data", xformedData);

        setChartData(xformedData);
        return xformedData;
      } catch (error) {
        console.error("Error fetching history data", error);
      }
    };
    fetchHistory().then((data) => {
      new Chart(ctx, {
        type: "candlestick",
        data: {
          datasets: [
            {
              label: "Candlestick",
              data: data,
              barPercentage: 0.1, // Adjust this value to control the width
              categoryPercentage: 0.1, // Adjust for overall category width
            },
          ],
        },
        options: {
          responsive: true,
          scales: {
            x: {
              type: "time",
              time: {
                unit: "day",
                tooltipFormat: "ll", // Tooltip format for better readability
                display: true, // Ensure x-axis is displayed
              },
              title: {
                display: true,
                text: "Date",
              },
            },
            y: {
              display: true, // Ensure y-axis is displayed
              beginAtZero: false, // Set to false to avoid the 0 to 1 range
              title: {
                display: true,
                text: "Price",
              },
              /* ticks: {
                // Adjust y-axis ticks based on your data range
                callback: function (value) {
                  return "$" + value;
                },
              }, */
            },
          },
        },
      });
    });
  }, []);

  return <canvas ref={chartRef} width="1200" height="500"></canvas>;
};

export default StockChart;
