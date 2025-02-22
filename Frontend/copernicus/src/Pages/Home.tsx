import React from "react";
import "../styles/Home.css";

export const Home = () => {
  return (
    <div className="container-fluid bg">
        <div>
          <h1 className="text-light">Welcome to Copernicus</h1>
          <p className="text-light">
            This is a simple website for watching securities in your portfolio.
          </p>
          <p>
            <button className="btn btn-primary">Learn more</button>
          </p>
        </div>
    </div>
  );
};
